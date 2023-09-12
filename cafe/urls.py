from django.urls import path
from cafe import views

app_name = 'cafe'

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
]

