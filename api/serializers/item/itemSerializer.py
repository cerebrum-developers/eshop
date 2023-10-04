from rest_framework import serializers
from api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Create, Update, Retrieve, Delete Items
    """

    class Meta:
        model = Item
        fields = ('id', 'item_name', 'cost_price', 'selling_price', 'description', 'sale_tax')


class ItemDetailSerializer(serializers.ModelSerializer):
    """
    Create, Update, Retrieve, Delete Items
    """

    class Meta:
        model = Item
        fields = ('id', 'item_name', 'cost_price', 'selling_price', 'description', 'sale_tax')

class ItemSerializerPagination(serializers.ModelSerializer):
    """
    return items
    """

    class Meta:
        model = Item
        fields = ('id', 'item_name', 'cost_price', 'selling_price', 'description', 'sale_tax')