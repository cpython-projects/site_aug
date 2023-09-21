from .models import MainMenuItem, Footer


def main_menu_items(request):
    items = MainMenuItem.objects.filter(is_visible=True)
    return {'main_menu_items': items}


def footer(request):
    footer_items = Footer.objects.first()
    return {'footer_items': footer_items}