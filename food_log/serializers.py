from rest_framework import serializers

from food_log.models import Expense
class CalorieSerializers(serializers.ModelSerializer):

    class Meta:
        model=Expense
        fields="__all__"
        read_only_fields=["id","owner","created_at"]