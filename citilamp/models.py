
from django.db import models

# Create your models here


class CountryAndCityAttractions(models.Model):
    """
    Base class for attractions like zoos, restaurants, hotels etc of countries and cities
    """
    name = models.CharField(primary_key=True,max_length=450,null=False)
    #city_or_country = models.ForeignKey(City, on_delete=models.CASCADE) or models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.TextField()
    website = models.URLField()
    #details what can be done in this place
    details = models.TextField()
    def __str__(self):
        return self.name
"""
class ParksAndMuseums(CountryAndCityAttractions):
    pass
class ShopsAndMarkets(CountryAndCityAttractions):
    pass
class Hotels(CountryAndCityAttractions):
    pass
"""
class CountryAndCityInfo(models.Model):
    """
    This is the base class for info shared by countries and cities like
    Politics,Sleep,etiquettes etc.
    """
    travel_choices = (
        ('Air', 'By Air'),
        ('Plane', 'By Plane'),
        ('Bus', 'By Boat '),
        ('Train', 'By Train')
    )
    entry_requirement = models.CharField(max_length=250,choices=travel_choices)
    terrain = models.TextField()
    history = models.TextField()
    pre_colonial_era = models.TextField()
    post_independence= models.TextField()
    region = models.TextField()
    parks = CountryAndCityAttractions()
    tourist_centers = CountryAndCityAttractions()
    beaches = CountryAndCityAttractions()
    museums = CountryAndCityAttractions()
    galleries = CountryAndCityAttractions()
    markets_tradingCenters_shops = CountryAndCityAttractions()
    talks_and_language = models.TextField()
    politics_ruler_government = models.TextField()
    contact = models.TextField()
    respects = models.TextField()
    stayhealthy = models.TextField()
    lgbt = models.TextField()
    staysafe = models.TextField()
    work = models.TextField()
    education = models.TextField()
    sleep = models.TextField()
    drinks_eat = models.TextField()
    bargaining = models.TextField()
    buys = models.TextField()
    holiday = models.TextField()
    electricity = models.TextField()
    law_bureaucracy = models.TextField()
    historical_attraction = CountryAndCityAttractions()
    etiquettes = models.TextField()
    exchange  = models.TextField()
    cost = models.TextField()
    tipping = models.TextField()
    culture = models.TextField()
    measurement = models.TextField()
    planning_prearrival = models.TextField()
    documentation_visa = models.TextField()
    processing = models.TextField()
    corruption_crime = models.TextField()
    homosexuals_lesbian = models.TextField()
    drug = models.TextField()
    racism = models.TextField
    curfew = models.TextField
    animal_hunting = models.TextField()
    prostitute = models.TextField()
    fun_games_relaxation= models.TextField()
    excursion = models.TextField()
# Continent Model
class Continent(models.Model):

    name = models.CharField(max_length=200,primary_key=True,unique=True)
    image = models.ImageField(
                                width_field="width_field",
                                height_field="height_field")
    height_field = models.IntegerField(default=200)
    width_field = models.IntegerField(default=319)
    history = models.TextField()
    geo_loc = models.TextField()
    region = models.CharField(max_length=200)
    climate = models.TextField()
    continent_map = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Country(models.Model, CountryAndCityInfo):
    name = models.CharField(primary_key=True,max_length=250)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class State_Province(models.Model):

    name = models.CharField(primary_key=True, max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    best_city = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class City(models.Model, CountryAndCityInfo):

    name = models.CharField(primary_key=True,max_length=250)
    state_province = models.ForeignKey(State_Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
