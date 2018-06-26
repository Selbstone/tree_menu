from django import template
from django_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    # get all menu items in one query
    menu_items_set = MenuItem.objects.filter(name_menu=name).order_by("path").select_related('parent')

    # transformation in tree
    nodes = list(menu_items_set)
    tree = build_tree(nodes)

    return {'menu_items': tree, 'context': context}

def build_tree(nodes):
    tree = {}
    build_tree_recursive(tree, None, nodes)
    return tree

def build_tree_recursive(tree, parent, nodes):
    children = [n for n in nodes if n.parent == parent]
    for child in children:
        tree[child] = {}
        build_tree_recursive(tree[child], child, nodes)