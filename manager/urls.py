from django.urls import path
from .views import reservation_list

app_name = 'manager'

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
]

