from django import template
from django.urls import resolve, reverse
from ..models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/display_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
        current_url = context['request'].path
        def is_ancestor(item):
            if current_url == item.get_url():
                return True
            for child in item.children.all():
                if is_ancestor(child):
                    return True
            return False

        for item in menu.items.all():
            item.is_ancestor = is_ancestor(item)
        return {
            'menu': menu,
            'current_url': current_url,
        }
    except Menu.DoesNotExist:
        return {'menu': None}