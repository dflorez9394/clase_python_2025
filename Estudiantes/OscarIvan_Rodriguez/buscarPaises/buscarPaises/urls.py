from django.urls import path
from .views import (
    HealthView, CountryListAll, CountryFind,
    CountryCSVDownload, CountryCSVLoad, CountryCSVSave
)

urlpatterns = [
    path("health", HealthView.as_view()),
    path("countries/all", CountryListAll.as_view()),
    path("countries/find", CountryFind.as_view()),
    path("countries/csv", CountryCSVDownload.as_view()),
    path("countries/load", CountryCSVLoad.as_view()),
    path("countries/save", CountryCSVSave.as_view()),
]