from django.db import models
from modules.core.models import ModelBase, Location


# Create your models here.
class LicensePlate(ModelBase):
    plate_number = models.CharField(max_length=20, unique=True, verbose_name="License Plate")

    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = 'License Plate'
        verbose_name_plural = 'License Plates'
        db_table = 'license_plates'


class TollRecord(ModelBase):
    license_plate = models.ForeignKey(LicensePlate, on_delete=models.CASCADE, verbose_name="License Plate")
    pass_date = models.DateTimeField(verbose_name="Pass Date")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Location")
    image = models.ImageField(upload_to='toll_records', verbose_name="Image")

    def __str__(self):
        return '{}'.format(self.license_plate.plate_number)

    class Meta:
        verbose_name = 'Toll Record'
        verbose_name_plural = 'Toll Records'
        db_table = 'toll_records'
