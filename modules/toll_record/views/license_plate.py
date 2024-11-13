from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from modules.toll_record.models import LicensePlate
from modules.toll_record.forms.license_plate import LicensePlateForm
from django.urls import reverse_lazy
import re


class LicensePlateCreateView(LoginRequiredMixin, CreateView):
    model = LicensePlate
    template_name = 'license_plate/page-create.html'
    form_class = LicensePlateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        license_plate = form.cleaned_data['plate_number']
        if not re.match(r'^[A-Za-z]{3}-\d{3}$', license_plate):
            form.add_error('plate_number', 'El formato debe ser 3 letras - 3 números (ej: ABC-123).')
            return self.form_invalid(form)
        return super().form_valid(form)
