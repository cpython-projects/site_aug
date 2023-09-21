from django.shortcuts import render, redirect
from .models import DishCategory, Gallery, ContactInfoItem, Event
from django.views.generic import TemplateView
from .forms import ReservationForm, ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


class MainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = DishCategory.objects.filter(is_visible=True)
        context['gallery'] = Gallery.objects.filter(is_visible=True).order_by('?')[:4]
        context['booking_form'] = ReservationForm()
        context['title'] = 'Yummy'
        context['contacts_info'] = ContactInfoItem.objects.all()
        context['events'] = Event.objects.filter(models.Q(is_visible=True) &
                                                 (models.Q(date_time__isnull=True) |
                                                  models.Q(date_time__date__gte=timezone.now())))
        context['contact_form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        booking_form = ReservationForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

            send_mail(
                'Сообщение с контактной формы',
                f'Имя: {name}\nEmail: {email}\nСообщение: {message}',
                f'{email}',
                ['oleg.s.tymchuk@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Сообщение успешно отправлено')
            return redirect('cafe:home')

        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Ваш заказ принят')
            return redirect('cafe:home')

        context = self.get_context_data()
        context['contact_form'] = contact_form
        context['booking_form'] = booking_form
        return render(request, self.template_name, context)