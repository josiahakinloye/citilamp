import  datetime

from django.db import models

from django.utils import timezone
# Create your models here.

class AdsError(Exception):
    pass

class Ads(models.Model):
    title = models.CharField(max_length=250,primary_key=True)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now().date())
    stop_date = models.DateField()
    owner = models.CharField(max_length=999,verbose_name="owner of ad")
    phone_number = models.IntegerField(max_length=11)
    email = models.EmailField()
    duration = models.DurationField()
    approved = models.BooleanField(default=False)

    def has_expired(self):
        """
        This checks if a particular has expired.So admins can know when to take out an ad
        :return: Bool
        """
        now = timezone.now()
        return now < self.stop_date

    has_expired.admin_order_field = "stop_date"
    has_expired.boolean = True
    has_expired.short_description = "Has Ad expired?"

    def save(self, *args, **kwargs):
        if self.stop_date < self.start_date:
            super(Ads, self).save(*args, **kwargs)
        else:
            raise AdsError("Stop date is less than start date")