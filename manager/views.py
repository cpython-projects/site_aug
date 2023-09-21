from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from cafe.models import Reservation
from .forms import ReservationEditForm
from django.urls import reverse_lazy

# Собственный миксин для проверки принадлежности пользователя к группе 'manager'
class ManagerAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


# Представление для списка бронирований
class ReservationListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy('login')
    model = Reservation
    template_name = 'book_list.html'
    context_object_name = 'reservations'


# Представление для редактирования бронирования
class ReservationUpdateView(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    login_url = '/login/'
    model = Reservation
    form_class = ReservationEditForm
    template_name = 'edit_reservation.html'
    success_url = reverse_lazy('manager:reservation_list')
