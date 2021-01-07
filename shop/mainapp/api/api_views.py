from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView    # для вывода информации в виде списка
from rest_framework.generics import RetrieveAPIView    # для вывода информации об одном конкретном объекте используя информацию из поля поиска lookup_field
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView    # получить список или создать список (GET, POST запросы)
from rest_framework.generics import UpdateAPIView    # модификация через API (PUT, DELETE запросы)
from rest_framework.generics import DestroyAPIView    # удаление (DELETE запрос)
from rest_framework.filters import SearchFilter    # более гибкий вариант фильтрования
from rest_framework.pagination import PageNumberPagination    # для пагинации (2ой способ)

from .serializers import CategorySerializer, SmartphoneSerializer, NotebookSerializer, CustomerSerializer
from ..models import Category, Smartphone, Notebook, Customer


class ProductsPagination(PageNumberPagination):    # пагинация с использованием существующих классов пагинации (2ой способ)
    page_size = 2    # количество объектов на странице
    page_size_query_param = "page_size"    # указывающее имя параметра запроса, которое позволяет клиенту устанавливать размер страницы для каждого запроса
    max_page_size = 10    # максимально допустимый размер запрашиваемой страницы

    def get_paginated_response(self, data):    # для кастомизации вывода информации (результата пагинации) на пагинируемой странице (переопределение ключей)
        return Response(OrderedDict([
            ("Objects_count", self.page.paginator.count),
            ("next", self.get_next_link()),
            ("previous", self.get_previous_link()),
            ("items", data)
        ]))


class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):    # для вывода или создания списка категорий (почти поноценный крут)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    # выводит всю информацию о категориях


class SmartphoneListAPIView(ListAPIView):    # для вывода списка смартфонов
    serializer_class = SmartphoneSerializer
    pagination_class = ProductsPagination    # подключение класса пагинации к этому классу
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
    pagination_class = ProductsPagination
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
