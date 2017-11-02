# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# Continent Model
class Continent(models.Model):

    continent_name = models.CharField(max_length=200,primary_key=True)
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
        return self.continent_name

class Country(models.Model):
    name = models.CharField(primary_key=True)
    continent = models.ForeignKey(Continent)

    def __str__(self):
        return self.name

class State_Province(models.Model):

    name = models.CharField(primary_key=True)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

class City(models.Model):

    name = models.CharField(primary_key=True)
    state_province = models.ForeignKey(State_Province)

    def __str__(self):
        return self.name