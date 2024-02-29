from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Account, Transactions, FixedDeposit, Stock, Bond, MutualFund, Loan, ProvidentFund, Insurance

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'

class FixedDepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = FixedDeposit
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'

class BondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bond
        fields = '__all__'

class MutualFundSerializer(serializers.ModelSerializer):

    class Meta:
        model = MutualFund
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'

class ProvidentFundSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProvidentFund
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = '__all__'

