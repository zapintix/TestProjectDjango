from django import template
from menuapp.models import MenuItem

register = template.Library()

@register.simple_tag
def render_menu(menu_items=None):
    if menu_items is None:
        menu_items = MenuItem.objects.filter(parent=None)
    
    output = '<ul>'
    for item in menu_items:
        output += f'<li>{item.title}</li>'
        children = MenuItem.objects.filter(parent=item)
        if children.exists():
            output += render_menu(children)  # Рекурсивный вызов для дочерних элементов
    output += '</ul>'
    return output