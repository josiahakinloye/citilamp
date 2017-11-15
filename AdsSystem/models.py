from datetime import date

from django.db import models
from django.forms import ModelForm
# Create your models here.

class AdsError(Exception):
    pass

class Ads(models.Model):
    title = models.CharField(max_length=250,primary_key=True)
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    stop_date = models.DateField()
    owner_name = models.CharField(max_length=999,verbose_name="owner of ad")
    #todo use regex on client side to make sure interger phone number conforms to phone number
    owner_phone_number = models.IntegerField()
    owner_email = models.EmailField()
    duration = models.DurationField()
    approved = models.BooleanField(default=False)

    def has_expired(self):
        """
        This checks if a particular has expired.So admins can know when to take out an ad
        :return: Bool
        """

        return date.today() < self.stop_date

    has_expired.admin_order_field = "stop_date"
    has_expired.boolean = True
    has_expired.short_description = "Has Ad expired?"

    def save(self, *args, **kwargs):
        if date.today() <= self.start_date and self.stop_date > self.start_date:
            super(Ads, self).save(*args, **kwargs)
        else:
            raise AdsError("Ensure start date is more not less than today and stop date is greater than start date")

    def __str__(self):
        return self.title + "by"+ self.owner_name


class NewAdsForm(ModelForm):
    class Meta:
        model = Ads
        exclude = ['approved']