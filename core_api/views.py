from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from core.models import Category, Item, Order
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import (
    UserSerializer, OrderSerializer, ItemSerializer, CategorySerializer, 
    CreateOrderSerializer, CreateItemSerializer, UserPastOrdersSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(APIView):
    def get(self, request, **kwargs):
        username = self.kwargs['username']
        if(User.objects.filter(username=username).exists()):
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response({"user details": serializer.data})
        else:
            return Response({"user details": "user does not exists"})

class UserCurrentOrder(APIView):

    def get(self, request, **kwargs):
        username = self.kwargs['username']
        last_order = Order.objects.filter(user__username=username).latest('ordered_at')
        if(last_order.status == 'received' or last_order.status == 'cooking'):
            serializer = OrderSerializer(last_order)
            return Response({"current order status": serializer.data})
        else:
            return Response({"current order status": "user don't have any current order"})   
            
class UserPastOrders(generics.ListAPIView):
    serializer_class = UserPastOrdersSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        past_orders = Order.objects.filter(user__username=username).order_by('-ordered_at')
        return past_orders    

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderCreate(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        total_price = 0;
        discounts = self.request.data.get("discounts")
        items = self.request.data.getlist("items")
        for item in items:
            total_price += Item.objects.get(id=item).price
        if(discounts.__len__()!=0):
            totol_price -= int(discounts)    
        return serializer.save(total_price=max(0,total_price))

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ItemCreate(generics.CreateAPIView):
    serializer_class = CreateItemSerializer
    permission_classes = (IsAuthenticated,)

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SearchItemList(generics.ListAPIView):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer