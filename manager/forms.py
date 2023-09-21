from django import forms
from cafe.models import Reservation


class ReservationEditForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['is_processed', 'name', 'date', 'time', 'people']