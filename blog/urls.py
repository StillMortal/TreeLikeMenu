from django.contrib import admin
from django.urls import path
from my_blog.views import MenuListView, ItemByMenuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuListView.as_view(), name='menu-list'),
    path('<str:slug>/', ItemByMenuView.as_view(), name='item-by-menu'),
]