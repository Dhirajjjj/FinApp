import uuid

from django.db import models
from django.utils.timezone import now

# Account
class Account(models.Model):
    account_id = models.CharField(max_length=50, null=False, blank=False)
    account_balance = models.IntegerField(null=False, blank=False)
    account_holder_name = models.CharField(max_length=75, null=False, blank=False)
    account_type = models.CharField(max_length=20, null=False, blank=False)
    iso_currency_code = models.CharField(max_length=3, null=False, blank=False)
    account_limit = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now)

# Transactions
class Transactions(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(max_length=50, null=False, blank=False)
    transaction_type = models.CharField(max_length=20, null=False, blank=False)
    transaction_method = models.CharField(max_length=20, null=False, blank=False)
    transaction_amount = models.IntegerField(null=False, blank=False)
    transaction_date = models.CharField(max_length=20, null=True, blank=True)
    merchant_entity_id = models.UUIDField(default=uuid.uuid4, editable=False)
    iso_currency_code = models.CharField(max_length=3, null=False, blank=False)
    created_at = models.DateTimeField(default=now, editable=False)

# Investments
class FixedDeposit(models.Model):
    fixed_deposit_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(max_length=50, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    interest_rate = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    tenure_months = models.IntegerField(null=False, blank=False)
    maturity_amount = models.IntegerField(null=False, blank=False)
    maturity_date = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)

class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock_name =  models.CharField(max_length=50, null=False, blank=False)
    stock_symbol = models.CharField(max_length=50, null=False, blank=False)
    current_price = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    previous_close = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    volume = models.IntegerField(null=False, blank=False)
    market_cap = models.IntegerField(null=False, blank=False)
    pe_ratio = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)

class Bond(models.Model):
    bank_name = models.CharField(max_length=50, null=False, blank=False)
    bond_name = models.CharField(max_length=50, null=False, blank=False)
    face_value = models.IntegerField(null=False, blank=False)
    coupon_rate = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    maturity_date = models.CharField(max_length=50, null=False, blank=False)
    current_price = models.IntegerField(null=False, blank=False)
    yield_to_maturity = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)

class MutualFund(models.Model):
    fund_name = models.CharField(max_length=50, null=False, blank=False)
    fund_type = models.CharField(max_length=50, null=False, blank=False)
    fund_manager = models.CharField(max_length=50, null=False, blank=False)
    nav = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    fund_rating = models.CharField(max_length=50, null=False, blank=False)
    minimum_investment = models.IntegerField(null=False, blank=False)
    expense_ratio = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)

#Payments
class Loan(models.Model):
    loan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(max_length=50, null=False, blank=False)
    loan_amount = models.IntegerField(null=False, blank=False)
    interest_rate = models.IntegerField(null=False, blank=False)
    term_months = models.IntegerField(null=False, blank=False)
    start_date = models.CharField(max_length=50, null=False, blank=False)
    end_date = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)

class ProvidentFund(models.Model):
    ppf_account_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(max_length=50, null=False, blank=False)
    balance = models.IntegerField(null=False, blank=False)
    annual_contribution = models.IntegerField(null=False, blank=False)
    interest_rate = models.DecimalField(max_digits=12, decimal_places=6, null=False, blank=False)
    maturity_date = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)

class Insurance(models.Model):
    policy_number =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    policy_holder = models.CharField(max_length=50, null=False, blank=False)
    policy_type = models.CharField(max_length=50, null=False, blank=False)
    premium_amount = models.IntegerField(null=False, blank=False)
    coverage_amount = models.IntegerField(null=False, blank=False)
    start_date = models.CharField(max_length=50, null=False, blank=False)
    end_date = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)