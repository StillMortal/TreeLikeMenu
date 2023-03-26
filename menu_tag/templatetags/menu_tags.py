from django import template

from my_blog.models import Item


register = template.Library()


@register.inclusion_tag(filename='menu_tag/menu_items.html', takes_context=True)
def draw_menu(context, menu_name: str) -> dict:
    request_url = context['request'].build_absolute_uri()
    raw_menu_items = Item.objects.filter(menu__title=menu_name)

    items_dict = dict()
    root_items = list()
    current_items = list()

    for i_item in raw_menu_items:
        item_url = None

        items_dict[i_item.id] = {
            'menu_name': menu_name,
            'item_id': i_item.id,
            'title': i_item.title,
            'parent_id': None,
            'href': item_url,
            'expand': False,
            'children': list()
        }

        if request_url.endswith(str(item_url)):
            current_items.append(i_item.id)

    for item_id, item_value in items_dict.items():
        item_parent = items_dict[item_id]['parent_id']
        if item_parent is not None:
            items_dict[item_parent]['children'].append(item_value)
        else:
            root_items.append(item_value)

    for current_item_id in current_items:
        item = items_dict[current_item_id]

        item['expand'] = True

        parent = item['parent_id']

        while parent is not None:
            items_dict[parent]['expand'] = True
            parent = items_dict[parent]['parent_id']

    return {'menu_items': root_items, 'menu_name': menu_name}


@register.inclusion_tag(filename='menu_tag/list_of_items.html')
def menu_item(items: list) -> dict:
    return {'item_list': items}
