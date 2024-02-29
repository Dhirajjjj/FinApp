import requests

class Payments:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/account/payments"

    def get_loan_balance(self):
        url = self.base_url + '/loans'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        loan_amount = sum([item["loan_amount"] for item in data])

        monthly_loan_amount = loan_amount

        return monthly_loan_amount
    
    def get_provident_fund_balance(self):
        url = self.base_url + '/pf'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        annual_contribution = sum([item["annual_contribution"] for item in data])

        return annual_contribution

    def get_insurance_balance(self):
        url = self.base_url + '/insurance'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        premium_amount = sum([item["premium_amount"] for item in data])

        return premium_amount

    def get_payment_summary(self):
        loan_amount = self.get_loan_balance()
        pf_contibution = self.get_provident_fund_balance()
        insurance_premium = self.get_insurance_balance()

        return {
            "loan_amount": loan_amount,
            "provident_fund_contribution": pf_contibution,
            "insurance_premium": insurance_premium
        }