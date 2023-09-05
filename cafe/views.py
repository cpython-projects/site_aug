from django.shortcuts import render
from .models import DishCategory


def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    return render(request, 'main.html', context={'categories': categories})
