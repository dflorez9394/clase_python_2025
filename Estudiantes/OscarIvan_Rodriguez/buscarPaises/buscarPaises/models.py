from django.db import models

class Country(models.Model):
    # Nombre común del país. Único para evitar duplicados.
    name = models.CharField(max_length=150, unique=True)
    # Monedas en formato legible: "Colombian peso ($), Euro (€)"
    monedas = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name