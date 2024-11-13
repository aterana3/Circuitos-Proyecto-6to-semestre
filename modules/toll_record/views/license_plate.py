from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from modules.toll_record.models import LicensePlate
from modules.toll_record.forms.license_plate import LicensePlateForm
from django.urls import reverse_lazy
import re
from django.db.models import Q


class LicensePlateCreateView(LoginRequiredMixin, CreateView):
    model = LicensePlate
    template_name = 'license_plates/page-create.html'
    form_class = LicensePlateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        license_plate = form.cleaned_data['plate_number']
        if not re.match(r'^[A-Za-z]{3}-\d{3}$', license_plate):
            form.add_error('plate_number', 'El formato debe ser 3 letras - 3 números (ej: ABC-123).')
            return self.form_invalid(form)
        return super().form_valid(form)


class LicensePlateListView(LoginRequiredMixin, ListView):
    model = LicensePlate
    template_name = 'license_plates/page-list.html'
    context_object_name = 'license_plates'
    paginate_by = 10

    def get_queryset(self):
        self.query = Q()
        plate_number = self.request.GET.get('plate_number')
        if plate_number is not None:
            self.query &= Q(plate_number__icontains=plate_number)
        return LicensePlate.objects.filter(self.query).order_by('id')