from rest_framework import serializers

from .models import FinancialTransaction


class FinancialTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTransaction
        fields = ["type", "date", "value", "cpf",
                  "card", "hour", "store_owner", "store_name"]

        def create(self, validated_data: dict) -> FinancialTransaction:
            return FinancialTransaction.objects.create(**validated_data)


class FinancialTransactionStoreSerializer(serializers.ModelSerializer):
    total_balance = serializers.FloatField()

    class Meta:
        model = FinancialTransaction
        fields = ["store_name", "store_owner", "total_balance"]
