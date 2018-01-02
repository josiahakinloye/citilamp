from datetime import date, timedelta

from django.test import TestCase
from . models import Ads, AdsError

class AdsTestCase(TestCase):
    """
    This class tests the test of the Ads model
    """
    def setUp(self):
        # start_date by default is date.today()
        self.test_ad = Ads(title='Test', description='test',
                     owner_name='test', owner_phone_number='1234567890',
                     owner_email='test@test.com'
                     )

    def test_can_ad_save(self):
        self.test_ad.stop_date  = date.today()+timedelta(days=1)
        self.test_ad.save()
        self.assertQuerysetEqual(Ads.objects.all(), ['<Ads: Test by test>'])


    def test_cannot_save_with_bad_start_date(self):
        self.test_ad.start_date = date.today() - timedelta(days=1)
        self.test_ad.stop_date = date.today() + timedelta(days=1)
        with self.assertRaises(AdsError) as save_error:
            self.test_ad.save()
            self.assertEquals(save_error.msg, "Ensure start date is not less than today and stop date is greater than start date")


    def test_cannot_save_with_bad_stop_date(self):
        self.test_ad.stop_date = date.today() - timedelta(days=1)
        with self.assertRaises(AdsError) as save_error:
            self.test_ad.save()
            self.assertEquals(save_error.msg, "Ensure start date is not less than today and stop date is greater than start date")
