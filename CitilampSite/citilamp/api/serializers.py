from rest_framework import serializers
from ..models import *
class ContinentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Continent
        fields = ()
