from datetime import date
import re

from django.db import models
from django.forms import ModelForm, forms, TextInput
# Create your models here.
from django.forms.widgets import Input


class AdsError(Exception):
    pass

class Ads(models.Model):
    title = models.CharField(max_length=250,primary_key=True)
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    stop_date = models.DateField()
    owner_name = models.CharField(max_length=999,verbose_name="owner of ad")
    owner_phone_number = models.IntegerField()
    owner_email = models.EmailField()
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

class DATEINPUT(Input):
    input_type = 'date'


def is_this_a_valid_phoneNumber(number):
    """
    Validates this is a phone number
    :param number: Str note if zero is first digit it is removed ie 070xxx becomes 70xxx
    :return: Match object which is none if match fails
    """
    return re.match(r"^\d{10}$", number)

class NewAdsForm(ModelForm):
    class Meta:
        model = Ads
        exclude = ['approved']
        widgets = {
            'start_date': DATEINPUT,
            'stop_date' : DATEINPUT,
        }
    def clean_owner_phone_number(self):
        phone_number = str(self.cleaned_data['owner_phone_number'])
        if not is_this_a_valid_phoneNumber(phone_number):
            raise forms.ValidationError("Phone number is not valid ensure it is a 10 digit number with no extra characters befor or after it")
        return self.cleaned_data['owner_phone_number']