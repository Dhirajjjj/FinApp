import requests

class Transactions:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/api"

    def get_account_transactions(self):
        url = self.base_url + '/transactions'
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        debit = [trans.get('transaction_amount') for trans in data if trans.get('transaction_type') == 'debit']
        credit = [trans.get('transaction_amount') for trans in data if trans.get('transaction_type') == 'credit']
        upi = [trans.get('transaction_amount') for trans in data if trans.get('transaction_method') == 'UPI']

        total_transactions = len(data)
        debit_transactions = sum(debit)
        credit_transactions = sum(credit)
        upi_transactions = sum(upi)

        return {
            "total_transactions": total_transactions, 
            "debit_transactions_amount": debit_transactions,
            "credit_transactions_amount": credit_transactions,
            "upi_transactions_amount": upi_transactions
        }
