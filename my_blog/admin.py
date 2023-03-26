from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Menu


class ItemInline(admin.StackedInline):
    model = Item
    extra = 0
    fields = ['title', 'slug', 'menu', 'content']


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Item, ItemAdmin)


class MenuAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}

    inlines = ItemInline,


admin.site.register(Menu, MenuAdmin)