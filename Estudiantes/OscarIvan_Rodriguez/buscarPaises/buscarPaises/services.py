from __future__ import annotations
from typing import List, Dict
from pathlib import Path
import os
import csv
import httpx

from django.db import transaction
from .models import Country

REST_BASE = "https://restcountries.com/v3.1"
FIELDS = "name,currencies"  # pedimos solo lo necesario

def _currencies_to_list(curr: Dict) -> List[str]:
    if not curr:
        return []
    out = []
    for code, info in curr.items():
        cname = info.get("name") or code
        sym = info.get("symbol")
        out.append(f"{cname} ({sym})" if sym else cname)
    return out

async def search_countries_api(term: str) -> List[Dict]:
    url = f"{REST_BASE}/name/{term}?fullText=false&fields={FIELDS}"
    async with httpx.AsyncClient(timeout=20.0, headers={"User-Agent": "CountryFinderDjango/1.0"}) as client:
        r = await client.get(url)
        if r.status_code == 404:
            return []
        r.raise_for_status()
        items = r.json()

    results = []
    for it in items:
        name_obj = it.get("name") or {}
        common = name_obj.get("common") or ""
        curr = it.get("currencies") or {}
        if common:
            results.append({"name": common, "monedas": ", ".join(_currencies_to_list(curr))})
    return results

def csv_path() -> Path:
    # Permite configurar con .env -> CSV_PATH=paises.csv
    return Path(os.getenv("CSV_PATH", "paises.csv"))

def load_from_csv() -> int:
    """
    Lee CSV delimitado por | con encabezado: name|monedas
    Inserta evitando duplicados (único por name).
    """
    path = csv_path()
    if not path.exists():
        return 0
    inserted = 0
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="|")
        with transaction.atomic():
            for row in reader:
                name = (row.get("name") or "").strip()
                monedas = (row.get("monedas") or "").strip()
                if not name:
                    continue
                # get_or_create con case-insensitive
                obj, created = Country.objects.get_or_create(
                    name__iexact=name,
                    defaults={"name": name, "monedas": monedas}
                )
                if not created and monedas and (obj.monedas != monedas):
                    obj.monedas = monedas
                    obj.save(update_fields=["monedas"])
                if created:
                    inserted += 1
    return inserted

def save_to_csv() -> int:
    """
    Escribe CSV delimitado por | con encabezado: name|monedas
    """
    path = csv_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    qs = Country.objects.all().order_by("name")
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(["name", "monedas"])
        for c in qs:
            writer.writerow([c.name, c.monedas or ""])
    return qs.count()
