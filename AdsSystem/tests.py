from datetime import date, timedelta

from django.test import TestCase
from . models import Ads

class AdsTestCase(TestCase):
    """
    This class tests the test of the Ads model
    """
    def test_create_ad(self):
        Ads.objects.create(title='Test',description='test', stop_date= date.today()+timedelta(days=1),
                           owner_name='test', owner_phone_number ='1234567890' ,
                          owner_email='test@test.com'
                        )

        self.assertQuerysetEqual(Ads.objects.all(), ['<Ads: Test by test>'])