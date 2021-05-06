from django.db import models
from django.utils import timezone


class cylinder(models.Model):
    id=models.IntegerField(primary_key=True)
    address=models.CharField(max_length=200)
    Business_Name=models.CharField(max_length=200)
    person_Name=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    Verified_status=models.BooleanField()
    TimeStamp=models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name='cylinder'
        verbose_name_plural='cylinder'


