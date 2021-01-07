from rest_framework.generics import ListAPIView    # для вывода списка категорий

from .serializers import CategorySerializer
from ..models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    # выводит всю информацию о категориях
