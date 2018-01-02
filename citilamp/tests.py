from django.test import TestCase
from .models import CountryAndCityAttractions, City, Country
# Create your tests here.

class CitilampTestCase(TestCase):
    def setUp(self):
        self.test_attraction = CountryAndCityAttractions(name="Test Attraction")

    def test_attraction_must_have_city_or_country(self):
        with self.assertRaises(Exception) as attraction_error:
            self.test_attraction.save()
            self.assertEquals(attraction_error.msg, "Attraction must be linked to a country or a city")

    def test_attractions_must_not_have_city_and_country(self):
        self.test_attraction.country = Country(name='country')
        self.test_attraction.city = City(name='city')
        with self.assertRaises(Exception) as city_country_error:
            self.test_attraction.save()
            self.assertEquals(city_country_error.msg, "Attraction can only be tied to city or country not")
