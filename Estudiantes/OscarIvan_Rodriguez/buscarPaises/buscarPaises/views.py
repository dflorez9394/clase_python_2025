from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

from .models import Country
from .serializers import CountrySerializer
from .services import search_countries_api, load_from_csv, save_to_csv

class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})

class CountryListAll(APIView):
    def get(self, request):
        qs = Country.objects.all().order_by("name")
        return Response(CountrySerializer(qs, many=True).data)

class CountryFind(APIView):
    """
    GET /api/countries/find?name=col
    1) Busca en local (icontains).
    2) Si no hay resultados, consulta REST Countries, inserta evitando duplicados y devuelve.
    """
    async def get(self, request):
        term = (request.query_params.get("name") or "").strip()
        if not term:
            return Response({"detail": "Parámetro 'name' es requerido."}, status=400)

        # 1) Local
        local = Country.objects.filter(name__icontains=term).order_by("name")
        if local.exists():
            return Response(CountrySerializer(local, many=True).data)

        # 2) API
        results = await search_countries_api(term)
        if not results:
            return Response([], status=200)

        payload = []
        for item in results:
            name, monedas = item["name"], item.get("monedas", "")
            obj, created = Country.objects.get_or_create(
                name__iexact=name,
                defaults={"name": name, "monedas": monedas}
            )
            if not created and monedas and (obj.monedas != monedas):
                obj.monedas = monedas
                obj.save(update_fields=["monedas"])
            payload.append(obj)

        return Response(CountrySerializer(payload, many=True).data, status=200)

class CountryCSVDownload(APIView):
    """
    GET /api/countries/csv?name=Colombia -> CSV sólo de ese país
    GET /api/countries/csv               -> CSV de todos
    """
    def get(self, request):
        import io, csv
        name = (request.query_params.get("name") or "").strip()

        if name:
            qs = Country.objects.filter(name__iexact=name)
            if not qs.exists():
                return Response({"detail": "País no encontrado en local."}, status=404)
        else:
            qs = Country.objects.all().order_by("name")

        output = io.StringIO()
        writer = csv.writer(output, delimiter="|")
        writer.writerow(["name", "monedas"])
        for c in qs:
            writer.writerow([c.name, c.monedas or ""])
        data = output.getvalue().encode("utf-8")

        from django.http import HttpResponse
        resp = HttpResponse(data, content_type="text/csv; charset=utf-8")
        filename = f"paises_{name.lower() if name else 'todos'}.csv"
        resp["Content-Disposition"] = f'attachment; filename="{filename}"'
        return resp

class CountryCSVLoad(APIView):
    def post(self, request):
        added = load_from_csv()
        total = Country.objects.count()
        return Response({"added": added, "total": total})

class CountryCSVSave(APIView):
    def post(self, request):
        total = save_to_csv()
        return Response({"saved": total})
