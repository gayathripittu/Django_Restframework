from rest_framework import serializers
from passenger_App.models import passenger

class passengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=passenger
        fields= '__all__'


