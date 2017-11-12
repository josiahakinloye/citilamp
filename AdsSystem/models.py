import  datetime

from django.db import models

from django.utils import timezone
# Create your models here.

class AdsError(Exception):
    pass

class AdOwner(models.Model):
    name = models.CharField(primary_key=True,unique=True)
    address  = models.TextField()

class Ads(models.Model):
    title = models.CharField(max_length=250,primary_key=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now())
    stop_date = models.DateTimeField()
    owner = models.ForeignKey(AdOwner, on_delete=models.CASCADE)
    def is_valid(self):
        """
        This checks if a particular ad is valid.So admins can know when to take out an ad
        :return: Bool
        """
        now = timezone.now()
        return now < self.stop_date

    is_valid.admin_order_field = "stop_date"
    is_valid.boolean = True
    is_valid.short_description = "Is Ad still valid?"


    def save(self, *args, **kwargs):
        if self.stop_date < self.start_date:
            super(Ads, self).save(*args, **kwargs)
        else:
            raise AdsError("Stop date is less than start date")