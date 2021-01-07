from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):    # сериалайзер для модели Category
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category    # используемая модель
        fields = [    # поля
            "id", "name", "slug"
        ]
