from django.views.generic import ListView
from .models import Item, Menu


class MenuListView(ListView):
    model = Menu
    template_name = "my_blog/index.html"


class ItemByMenuView(ListView):
    context_object_name = 'items'
    template_name = 'my_blog/index.html'

    def get_queryset(self):
        self.menu = Menu.objects.get(slug=self.kwargs['slug'])
        queryset = Item.objects.filter(menu=self.menu)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.menu
        return context