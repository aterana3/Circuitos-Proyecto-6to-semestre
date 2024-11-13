from django.urls import path
from modules.toll_record.views.toll_record import TollRecordListView

app_name = 'toll_record'

urlpatterns = [
    path('', TollRecordListView.as_view(), name='toll_record_list'),
]