from rest_framework import serializers
from .models import cylinder

class cylinderserializer(serializers.ModelSerializer):
    class Meta:
        model=cylinder
        fields=['id','address','Business_Name','person_Name','contact','Verified_status','TimeStamp']
