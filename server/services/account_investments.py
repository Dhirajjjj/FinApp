import requests

class Investments:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api/account/investments"

    def get_fixed_deposit_balance(self):
        url = self.base_url + '/deposits'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        maturity_amount = [item["maturity_amount"] for item in data]
        next_maturity_date = [item["maturity_date"] for item in data]

        fixed_deposits = len(data)
        total_maturity_amount = sum(maturity_amount)
        next_maturity = next_maturity_date[0]

        return {
            "fixed_deposits": fixed_deposits, 
            "maturity_amount": total_maturity_amount,
            "next_maturity_date": next_maturity
        }
    
    def get_stock_balance(self):
        url = self.base_url + '/stocks'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        stock_amount = [item["current_price"] for item in data]
        stock_quantity = sum([item["volume"] for item in data])

        total_stock_amount = sum(int(float(num)) for num in stock_amount)

        return {
            "stock_amount": total_stock_amount,
            "stock_quantity": stock_quantity
        }

    def get_bond_balance(self):
        url = self.base_url + '/bonds'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        maturity_amount = sum([item["current_price"] for item in data])
        next_maturity_date = [item["maturity_date"] for item in data]

        return {
            "maturity_amount": maturity_amount,
            "next_maturity_date": next_maturity_date[0]
        }
    
    def get_mutual_fund_balance(self):
        url = self.base_url + '/mutualfunds'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        total_funds = len(data)
        nav = [item["nav"] for item in data]
        fund_amount = sum([item["minimum_investment"] for item in data]) + sum(int(float(num)) for num in nav)

        return {
            "total_funds": total_funds,
            "mutual_fund_amount": fund_amount
        }

    def get_investment_summary(self):
        fixed_deposits = self.get_fixed_deposit_balance()
        stocks = self.get_stock_balance()
        bonds = self.get_bond_balance()
        mutual_funds = self.get_mutual_fund_balance()

        return {
            "fixed_deposits": fixed_deposits['fixed_deposits'], 
            "deposit_maturity_amount": fixed_deposits['maturity_amount'],
            "next_deposit_maturity_date": fixed_deposits['next_maturity_date'],
            "stock_amount": stocks['stock_amount'],
            "stock_quantity": stocks['stock_quantity'],
            "bond_maturity_amount": bonds['maturity_amount'],
            "next_bond_maturity_date": bonds['next_maturity_date'],
            "total_funds": mutual_funds['total_funds'],
            "mutual_fund_amount": mutual_funds['mutual_fund_amount']
        }