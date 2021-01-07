from rest_framework import serializers

from ..models import Category, Smartphone, Notebook


class CategorySerializer(serializers.ModelSerializer):    # сериалайзер для модели Category
    name = serializers.CharField(required=True)    # required - обязательно или не обязательно должен присутствовать или быть заполненым
    slug = serializers.SlugField()

    class Meta:
        model = Category    # используемая модель
        fields = [    # поля
            "id", "name", "slug"
        ]


class BaseProductSerializer:
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)    # вместо ForeignKey (передается queryset в котороб будет осуществлятся поиск)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)    # В сериалайзерах нет TextField, заменить на CharField
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    resolution = serializers.CharField(required=True)
    accum_volume = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    rom = serializers.CharField(required=True)
    sd = serializers.BooleanField(required=True)
    sd_volume_max = serializers.CharField(required=False)
    main_cam_mp = serializers.CharField(required=True)
    frontal_cam_mp = serializers.CharField(required=True)

    class Meta:
        model = Smartphone
        # fields = [
        #     "category", "title", "slug", "image", "description",
        #     "price", "diagonal", "display_type", "resolution", "accum_volume",
        #     "ram", "rom", "sd", "sd_volume_max", "main_cam_mp", "frontal_cam_mp"
        # ]
        fields = "__all__"    # выбрать все поля


class NotebookSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    processor_freq = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    video = serializers.CharField(required=True)
    time_without_charge = serializers.CharField(required=True)

    class Meta:
        model = Notebook
        fields = "__all__"
