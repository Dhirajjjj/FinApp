import requests
import random

BASE_URL = "http://127.0.0.1:8000/api"

def generate_account_data():

    account_id = "1234"
    account_balance =  random.randint(2000, 50000)
    account_holder_name = "Josh Piere"
    account_type = "saving"
    iso_currency_code = "USD"
    account_limit = 5000
    
    return {
        "account_id": account_id,
        "account_balance": account_balance,
        "account_holder_name": account_holder_name,
        "account_type": account_type,
        "iso_currency_code": iso_currency_code,
        "account_limit": account_limit
    }

def generate_transaction_data():
    account_id = "1234"
    transaction_type = random.choice(["debit"] * 10 + ["credit"])
    transaction_method = random.choice(["digital"] + ["UPI"] * 2)
    transaction_amount = random.randint(12, 120)
    iso_currency_code = "USD"
    
    return {
        "account_id": account_id,
        "transaction_type": transaction_type,
        "transaction_method": transaction_method,
        "transaction_amount": transaction_amount,
        "iso_currency_code": iso_currency_code
    }

def generate_fixed_deposit_data():

    calculate_maturity_amount = lambda P, r, n: int(P * pow(1 + r / 100, n / 12))
    
    account_id = "1234"
    tenure_months = random.randint(6, 24)
    interest_rate = round(random.uniform(4 + 0.5, 12 - 0.5), 1)
    amount = random.randint(200, 1200)
    maturity_amount = calculate_maturity_amount(amount, interest_rate, tenure_months)
    status = "active"
    
    return {
        "account_id": account_id,
        "amount": amount,
        "interest_rate": interest_rate,
        "tenure_months": tenure_months,
        "maturity_amount": maturity_amount,
        "maturity_date": "2024-12-31",
        "status": status
    }

def generate_stock_data():
    
    current_price = round(random.uniform(140 + 0.5, 260 - 0.5), 1)
    previous_close = round(random.uniform(140 + 0.5, 260 - 0.5), 1)
    volume = random.randint(200, 1200)
    market_cap = random.randint(500000, 10000000)
    pe_ratio = round(random.uniform(12 + 0.5, 22 - 0.5), 1)
    
    return {
        "stock_name": "Adidas Inc",
        "stock_symbol": "ADI",
        "current_price": current_price,
        "previous_close": previous_close,
        "volume": volume,
        "market_cap": market_cap,
        "pe_ratio": pe_ratio
    }

def generate_bond_data():
    
    face_value = random.randint(500, 1500)
    coupon_rate = round(random.uniform(4 + 0.5, 8 - 0.5), 1)
    current_price = face_value + random.randint(25, 200)
    yield_to_maturity = round(random.uniform(3 + 0.5, 8 - 0.5), 1)
    
    return {
        "bank_name": "ICICI Bank",
        "bond_name": "ICICI Bank Series A Bond",
        "face_value": face_value,
        "coupon_rate": coupon_rate,
        "maturity_date": "2025-12-31",
        "current_price": current_price,
        "yield_to_maturity": yield_to_maturity
    }

def generate_mutual_fund_data():
    
    minimum_investment = random.randint(500, 1500)
    nav = round(random.uniform(140 + 0.5, 260 - 0.5), 1)
    expense_ratio = round(random.uniform(1 + 0.5, 6 - 0.5), 1)
    
    return {
        "fund_name": "ICICI Bank Equity Fund",
        "fund_type": "Equity",
        "fund_manager": "Ryan Nolan",
        "nav": nav,
        "fund_rating": "4 stars",
        "minimum_investment": minimum_investment,
        "expense_ratio": expense_ratio
    }

def generate_loan_data():
    
    loan_amount = random.randint(5000, 15000)
    interest_rate = random.randint(4, 12)
    term_months = 24
    
    return {
        "account_id": "1234",
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "term_months": term_months,
        "start_date": "2024-02-29",
        "end_date": "2026-02-28",
        "status": "active"
    }

def generate_provident_fund_data():
    
    balance_amount = random.randint(5000, 50000)
    interest_rate = round(random.uniform(4 + 0.5, 12 - 0.5), 1)
    annual_amount = balance_amount * (interest_rate / 100)
    
    return {
        "account_id": "1234",
        "balance": balance_amount,
        "annual_contribution":annual_amount,
        "interest_rate":interest_rate,
        "maturity_date": "2030-05-15",
        "status": "active"
    }

def generate_insurance_data():
    
    coverage_amount = random.uniform(500000, 5000000)
    premium_amount = 5 % coverage_amount
    
    return {
        "policy_holder": "Josh Piere",
        "policy_type": "Life Insurance",
        "premium_amount": premium_amount,
        "coverage_amount": coverage_amount,
        "start_date": "2023-01-01",
        "end_date": "2043-01-01",
        "status": "active"
    }

if __name__ == '__main__':

    for _ in range(1):
        account_data = generate_account_data()
        response = requests.post(BASE_URL + '/account', json=account_data)
    
    for _ in range(56):
        transaction_data = generate_transaction_data()
        response = requests.post(BASE_URL + '/transactions', json=transaction_data)
    
    for _ in range(3):
        transaction_data = generate_fixed_deposit_data()
        response = requests.post(BASE_URL + '/account/investments/deposits', json=transaction_data)

    for _ in range(5):
        transaction_data = generate_stock_data()
        response = requests.post(BASE_URL + '/account/investments/stocks', json=transaction_data)
    
    for _ in range(2):
        transaction_data = generate_bond_data()
        response = requests.post(BASE_URL + '/account/investments/bonds', json=transaction_data)
    
    for _ in range(2):
        transaction_data = generate_mutual_fund_data()
        response = requests.post(BASE_URL + '/account/investments/mutualfunds', json=transaction_data)
    
    for _ in range(2):
        transaction_data = generate_loan_data()
        response = requests.post(BASE_URL + '/account/payments/loans', json=transaction_data)
    
    for _ in range(2):
        transaction_data = generate_provident_fund_data()
        response = requests.post(BASE_URL + '/account/payments/pf', json=transaction_data)
    
    for _ in range(2):
        transaction_data = generate_insurance_data()
        response = requests.post(BASE_URL + '/account/payments/insurance', json=transaction_data)