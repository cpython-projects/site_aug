from django.urls import path
from .views import ReservationListView, ReservationUpdateView

app_name = 'manager'

urlpatterns = [
    path('reservation/list/', ReservationListView.as_view(), name='reservation_list'),
    path('reservation/edit/<int:pk>/', ReservationUpdateView.as_view(), name='edit_reservation'),
]
