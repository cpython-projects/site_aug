from django.shortcuts import render
from .models import DishCategory, Gallery
from django.views.generic import TemplateView

# def main_page(request):
#     if request.method == 'POST':
#         ...
#     elif request.method == 'GET':
#         categories = DishCategory.objects.filter(is_visible=True)
#         gallery = Gallery.objects.filter(is_visible=True).order_by('?')[:4]
#         return render(request, 'main.html', context={'categories': categories, 'gallery': gallery})


class MainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = DishCategory.objects.filter(is_visible=True)
        context['gallery'] = Gallery.objects.filter(is_visible=True).order_by('?')[:4]
        return context

    def post(self):
        ...


