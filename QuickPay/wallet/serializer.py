import uuid

from rest_framework import serializers

from wallet.models import Wallet


class WalletTransferSerializer(serializers.Serializer):
    receiver_wallet = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    idempotency_key = serializers.UUIDField() #generated from frontend automatically
    description=serializers.CharField(max_length=255, required=False)

    def validate_amount(self, value):
        if value < 0:
            raise Exception("Invalid amount. Amount cannot be greater than zero.")
        return value

    def validate_receiver_wallet(self, value):
        try:
            receiver_wallet = Wallet.objects.get(wallet_number=value)
        except Wallet.DoesNotExist:
            raise Exception("Wallet does not exist.")
        return receiver_wallet

class DepositSerializer(serializers.Serializer):

    amount = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)

    def validate_amount(self, value):
        if value < 0:
            raise Exception("Invalid amount. Amount cannot be greater than zero.")
        return value


class FundWalletSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_amount(self, value):
        if value < 0:
            raise Exception("Invalid amount. Amount cannot be lesser than zero.")
        return value