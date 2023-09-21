from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'error_pages/404.html', status=404)


def handler500(request):
    return render(request, 'error_pages/500.html', status=500)
