from django.urls import path
from .views import DepartmentApiView, IndexApiView, RegionsApiView, CountriesApiView


urlpatterns = [
    path('', IndexApiView.as_view()),

    path('countries', CountriesApiView.as_view()),
    path('countries/<int:country_id>/regions', RegionsApiView.as_view()),
    path('regions/<int:region_id>/departments', DepartmentApiView.as_view()),
]
