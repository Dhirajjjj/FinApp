import requests

class Account:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api"

    def get_account_balance(self):
        url = self.base_url + '/account'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        balance = [item["account_balance"] for item in response.json()]

        connected_accounts = len(data)
        total_account_balance = sum(balance)

        return {
            "connected_accounts": connected_accounts, 
            "total_account_balance": total_account_balance
        }
    
    def get_account_limit(self):
        pass
