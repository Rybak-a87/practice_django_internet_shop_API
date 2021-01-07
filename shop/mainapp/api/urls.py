from django.urls import path

from .api_views import CategoryListAPIView, SmartphoneListAPIView, NotebookListAPIView


app_name = "api"


urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="categories_api"),
    path("smartphones/", SmartphoneListAPIView.as_view(), name="smartphones_api"),
    path("notebooks/", NotebookListAPIView.as_view(), name="notebooks_api"),
]



