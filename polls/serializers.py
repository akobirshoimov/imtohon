from rest_framework import serializers 
from .models import KitoblarModel,AvtorlarModel

class KitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitoblarModel
        fields = ('name','page','pub_date')

class AvtorlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvtorlarModel
        fields = ('first_name','last_name','date_of_birth','combine')