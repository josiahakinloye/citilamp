import re

from django.forms import ModelForm, forms
from django.forms.widgets import Input

from .models import Ads


class DATEINPUT(Input):
    """
    Create a new html5 input element of type date
    """
    input_type = 'date'


def is_this_a_valid_phoneNumber(number):
    """
    Validates if number passed in is a Nigerian phone number
    :param number: Str note if zero is first digit it is removed ie 070xxx becomes 70xxx
    :return: Match object which is none if match fails
    """
    return re.match(r"^\d{10}$", number)

class NewAdForm(ModelForm):
    """
    Form that maps to the ad model
    """
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
            raise forms.ValidationError("Phone number is not valid ensure it is a 10 digit number")
        return self.cleaned_data['owner_phone_number']