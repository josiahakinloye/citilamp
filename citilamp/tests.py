from django.test import TestCase
from .models import CountryAndCityAttractions
# Create your tests here.

#todo : remove primrary keys in models
class citilampTestCase(TestCase):
    def test_attractions_has_city_or_country(self):
        test_attraction = CountryAndCityAttractions(name="Test Attraction")
        with self.assertRaises(Exception) as attraction_error:
            test_attraction.save()
            self.assertEqual(attraction_error.msg, "Attraction must be linked to a country or a city")
