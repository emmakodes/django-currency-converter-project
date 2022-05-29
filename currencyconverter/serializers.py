from rest_framework import serializers
from .models import Currency


class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["currency_value"]
