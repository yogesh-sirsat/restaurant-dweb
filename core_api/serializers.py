from rest_framework import serializers
from core.models import Category, Item, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ('id', 'name', 'image', 'description', 'category', 'price','size', 'veg')

class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'image', 'description', 'category', 'price', 'size', 'veg')

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'items', 'total_price', 'discounts', 'ordered_at')

class UserPastOrdersSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'status', 'items', 'total_price', 'discounts', 'ordered_at')        

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'items', 'total_price', 'discounts', 'ordered_at')