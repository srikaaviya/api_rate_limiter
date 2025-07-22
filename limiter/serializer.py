from rest_framework import serializers
from .models import RateLimit

class RateLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateLimit
        fields = '__all__'
