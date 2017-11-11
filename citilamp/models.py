
from django.db import models

# Create your models here


class CountryAndCityInfo(models.Model):
    """
    This is the base class for info shared by countries and cities like
    Politics,Sleep,etiquette etc.
    """
    travel_choices = (
        ('Air', 'By Air'),
        ('Plane', 'By Plane'),
        ('Bus', 'By Boat '),
        ('Train', 'By Train')
    )
    entry_requirement = models.CharField(max_length=250,choices=travel_choices,blank=True)
    history = models.TextField(blank=True)
    pre_colonial_era = models.TextField(blank=True)
    colonial_era = models.TextField(blank=True)
    post_independence= models.TextField(blank=True)
    terrain = models.TextField(blank=True)
    region = models.TextField(blank=True)
    talks_and_language = models.TextField(blank=True)
    politics_ruler_government = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    respects = models.TextField(blank=True)
    stay_healthy = models.TextField(blank=True)
    lgbt = models.TextField(blank=True)
    stay_safe = models.TextField(blank=True)
    work = models.TextField(blank=True)
    education = models.TextField(blank=True)
    sleep = models.TextField(blank=True)
    #todo: does drinks_eat mean resturants
    drinks_eat = models.TextField(blank=True)
    bargaining = models.TextField(blank=True)
    buys = models.TextField(blank=True)
    holiday = models.TextField(blank=True)
    electricity = models.TextField(blank=True)
    law_bureaucracy = models.TextField(blank=True)
    etiquettes = models.TextField(blank=True)
    exchange  = models.TextField(blank=True)
    cost = models.TextField(blank=True)
    tipping = models.TextField(blank=True)
    culture = models.TextField(blank=True)
    measurement = models.TextField(blank=True)
    planning_preArrival_documentation_visaProcessing = models.TextField(blank=True)
    corruption_crime = models.TextField(blank=True)
    homosexuals_lesbian = models.TextField(blank=True)
    drug = models.TextField(blank=True)
    racism = models.TextField(blank=True)
    curfew = models.TextField(blank=True)
    animal_hunting = models.TextField(blank=True)
    prostitute = models.TextField(blank=True)
    fun_games_relaxation= models.TextField(blank=True)
    excursion = models.TextField(blank=True)

class Continent(models.Model):
    name = models.CharField(max_length=200,primary_key=True,unique=True)
    image = models.ImageField(
                                width_field="width_field",
                                height_field="height_field",blank=True)
    height_field = models.IntegerField(default=200, blank=True)
    width_field = models.IntegerField(default=319, blank=True)
    history = models.TextField(blank=True)
    geo_loc = models.TextField(blank=True)
    region = models.CharField(max_length=200, blank=True)
    climate = models.TextField(blank=True)
    continent_map = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Continents"

class Country(CountryAndCityInfo):
    name = models.CharField(primary_key=True,max_length=250)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"

class StateProvince(models.Model):

    name = models.CharField(primary_key=True, max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    best_city = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "States And Provinces"

class City(CountryAndCityInfo):

    name = models.CharField(primary_key=True,max_length=250)
    stateprovince = models.ForeignKey(StateProvince, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Cities"

class CountryAndCityAttractions(models.Model):
    """
    Base class for attractions like zoos, restaurants, hotels etc of countries and cities
    """
    name = models.CharField(primary_key=True, max_length=450, null=False)
    city= models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True,null=True)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)
    #what can be done in this place
    details = models.TextField(blank=True)

    #check that the attraction was tied to a city or a country not both, if not do not save

    def save(self, *args, **kwargs):
        if self.city  or  self.country:
            if self.city and self.country:
                raise Exception("Attraction can only be tied to city or country not both")
            else:
                super(CountryAndCityAttractions, self).save(*args, **kwargs)
        else:
            raise Exception("Attraction must be linked to a country or a city")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Park(CountryAndCityAttractions):
    pass
class TouristCenter(CountryAndCityAttractions):
    pass
class Beach(CountryAndCityAttractions):
    class Meta:
        verbose_name_plural = "Beaches"
class Museum(CountryAndCityAttractions):
    pass
class Gallery(CountryAndCityAttractions):
    class Meta:
        verbose_name_plural = "Galleries"
class MarketTradingcenterSHOP(CountryAndCityAttractions):
    class Meta:
        verbose_name_plural = "Markets, Trading centers and Shops "
class HistoricalAttraction(CountryAndCityAttractions):
    pass