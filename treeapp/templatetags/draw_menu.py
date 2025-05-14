# draw_menu.py
from django import template
from treeapp.models import Menu, MenuItem

register = template.Library()

def build_tree(items, parent=None, active_ids=set()):
    tree = []
    for item in items:
        if item.parent == parent:
            children = build_tree(items, item, active_ids)
            item.cchildren = children
            item.is_active = item.id in active_ids
            item.is_open = any(getattr(child, 'is_active', False) or getattr(child, 'is_open', False) for child in children)
            tree.append(item)
    return tree

def find_active_ids(items, current_url):
    active_ids = set()
    for item in items:
        if item.get_absolute_url() == current_url:
            current = item
            while current:
                active_ids.add(current.id)
                current = current.parent
    return active_ids

@register.inclusion_tag("treeapp/menu_include.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    try:
        menu = Menu.objects.get(name=menu_name)
        items = MenuItem.objects.filter(menu=menu).select_related('parent')
        active_ids = find_active_ids(items, current_url)
        tree = build_tree(items, parent=None, active_ids=active_ids)
        return {
            'menu_items': tree,
            'current_url': current_url,
            'active_ids': active_ids,
        }
    except Menu.DoesNotExist:
        return {'menu_items': []}
