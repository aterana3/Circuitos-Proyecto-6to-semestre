from django.forms import ModelForm
from modules.toll_record.models import LicensePlate

class LicensePlateForm(ModelForm):
    class Meta:
        model = LicensePlate
        fields = '__all__'
        exclude = ['created_at', 'updated_at']