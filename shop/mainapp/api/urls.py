from django.urls import path

from .api_views import CategoryListAPIView


app_name = "api"


urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="categories_api")
]



