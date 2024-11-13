from django.urls import path
from modules.toll_record.views.toll_record import TollRecordListView
from modules.toll_record.views.license_plate import LicensePlateCreateView

app_name = 'toll_record'

urlpatterns = [
    path('', TollRecordListView.as_view(), name='toll_record_list'),
    path('/lincense_plate/create', LicensePlateCreateView.as_view(), name='license_plate-create'),
]