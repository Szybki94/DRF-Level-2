from rest_framework import serializers
from apps.quotes.models import Quote


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
