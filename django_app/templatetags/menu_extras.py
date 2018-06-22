from django import template
from django_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    root_item = MenuItem.objects.filter(name_item=name)
    return {'menu_items': root_item, 'context': context}