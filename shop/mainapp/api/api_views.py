from rest_framework.generics import ListAPIView    # для вывода информации в виде списка
from rest_framework.generics import RetrieveAPIView    # для вывода информации об одном конкретном объекте используя информацию из поля поиска lookup_field
from rest_framework.filters import SearchFilter    # более гибкий вариант фильтрования
from .serializers import CategorySerializer, SmartphoneSerializer, NotebookSerializer, CustomerSerializer
from ..models import Category, Smartphone, Notebook, Customer


class CategoryListAPIView(ListAPIView):    # для вывода списка категорий
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    # выводит всю информацию о категориях


class SmartphoneListAPIView(ListAPIView):
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()

    # def get_queryset(self):    # фильтрация через переопределения queryset параметров (1ый способ)
    #     qs = super().get_queryset()
    #     price = self.request.query_params.get("price")    # фильтр по цене
    #     title = self.request.query_params.get("title")    # фильтр по названию
    #     search_params = {
    #         "price__iexact": price,    # iexact - точное совпадение
    #         "title__iexact": title
    #     }
    #     return qs.filter(**search_params)

    filter_backends = [SearchFilter]    # фильтрация по filter_backends - более гипкий способ фильтрации (2ой способ)
    search_fields = ["price", "title"]    # по каким параметрам фильтровать (указывать ?search=<параметр фильтрации>)


class NotebookListAPIView(ListAPIView):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()

    filter_backends = [SearchFilter]    # фильтр
    search_fields = ["price", "title"]


class SmartphoneDetailAPIView(RetrieveAPIView):    # для вывода информации об одном конкретном объекте используя информацию из поля поиска lookup_field
    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    lookup_field = "id"    # поле поиска для вывода


class NotebookDetailAPIView(RetrieveAPIView):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    lookup_field = "id"


class CustomersListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

