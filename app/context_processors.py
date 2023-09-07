from .models import Footer


def footer(request):
    footer_items = Footer.objects.first()
    return {'footer_items': footer_items}