from django.urls import path

from .api_views import (
    CategoryAPIView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    SmartphoneDetailAPIView,
    NotebookDetailAPIView,
    CustomersListAPIView,
)


app_name = "api"


urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="categories_list_create_api"),
    path("customers/", CustomersListAPIView.as_view(), name="customers_list_api"),
    path("smartphones/", SmartphoneListAPIView.as_view(), name="smartphones_list_api"),
    path("notebooks/", NotebookListAPIView.as_view(), name="notebooks_list_api"),
    path("smartphones/<str:id>/", SmartphoneDetailAPIView.as_view(), name="smartphone_detail_api"),
    path("notebooks/<str:id>/", NotebookDetailAPIView.as_view(), name="smartphone_detail_api"),
]



