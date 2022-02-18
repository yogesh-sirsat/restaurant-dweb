from django.conf.urls.static import static
from django.urls import path, include, re_path
from restaurant import settings
from django.views.static import serve
from .views import (
    UserDetail, UserList, CategoryDetail, CategoryList, OrderDetail,
    OrderList, ItemDetail, ItemList, UserCurrentOrder, UserPastOrders,
    OrderCreate, ItemCreate
)
urlpatterns = [
    path('user/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('user/', UserList.as_view(), name='userlist'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='categorydetail'),
    path('category/', CategoryList.as_view(), name='categorylist'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='ordersdetail'),
    path('orders/', OrderList.as_view(), name='orderslist'),
    path('orders/create', OrderCreate.as_view(), name='ordercreate'),
    path('menuitems/<int:pk>/', ItemDetail.as_view(), name='menuitemsdetail'),
    path('menuitems/', ItemList.as_view(), name='menuitemslist'),
    path('menuitems/create', ItemCreate.as_view(), name='menuitemcreate'),
    path('user/<str:username>/current-order', UserCurrentOrder.as_view(), name='usercurrentorder'),
    path('user/<str:username>/orders', UserPastOrders.as_view(), name='userpastorders'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)