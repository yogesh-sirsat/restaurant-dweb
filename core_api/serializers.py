from rest_framework import serializers
from core.models import Profile, Category, Item, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ('id', 'name', 'image', 'description', 'category', 'price', 'discounts', 'size', 'veg')

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'status', 'items', 'total_price', 'discounts', 'ordered_at')
