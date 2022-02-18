from django.conf.urls.static import static
from django.urls import path, include, re_path
from restaurant import settings
from django.views.static import serve
from .views import CategoryDetail, CategoryList, OrderDetail, OrderList, ItemDetail, ItemList

urlpatterns = [
    path('category/<int:pk>/', CategoryDetail.as_view(), name='categorydetail'),
    path('category/', CategoryList.as_view(), name='categorylist'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='ordersdetail'),
    path('orders/', OrderList.as_view(), name='orderslist'),
    path('menuitems/<int:pk>/', ItemDetail.as_view(), name='menuitemsdetail'),
    path('menuitems/', ItemList.as_view(), name='menuitemslist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)