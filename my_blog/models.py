from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='item title')
    slug = models.SlugField(max_length=150)
    menu = TreeForeignKey('Menu', on_delete=models.PROTECT, related_name='items', verbose_name='Меню')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class Menu(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='menu title')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительское меню')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse('item-by-menu', args=[str(self.slug)])

    def __str__(self):
        return self.title