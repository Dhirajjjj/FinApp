from datetime import datetime

from services.account_balance import Account
from services.account_transactions import Transactions
from services.account_investments import Investments
from services.account_payments import Payments

class AccountSummary:

    def __init__(self):
        self.transactions = Transactions()
        self.account = Account()
        self.investments = Investments()
        self.payments = Payments()
        self.today = datetime.today()

    def generate_summary(self):
        account_balance = self.account.get_account_balance()
        account_transactions = self.transactions.get_account_transactions()
        account_investments = self.investments.get_investment_summary()
        account_payments = self.payments.get_payment_summary()

        formatted_date = self.today.strftime("%d/%m/%Y")

        message = f"""
FinApp : {formatted_date}

Accounts: {account_balance['connected_accounts']}
Current Balance: USD {account_balance['total_account_balance']}

TRANSACTIONS - (this month)
Transactions: {account_transactions['total_transactions']}
Debits: USD {account_transactions['debit_transactions_amount']}
Credits: USD {account_transactions['credit_transactions_amount']}
UPI Transactions: USD {account_transactions['upi_transactions_amount']}

INVESTMENTS
Fixed Deposits: USD {account_investments['deposit_maturity_amount']} ({account_investments['fixed_deposits']} deposits)
Next FD Maturity: {account_investments['next_deposit_maturity_date']}
Stock Portfolio: USD {account_investments['stock_amount']}
Bonds: USD {account_investments['bond_maturity_amount']}
Next Bond Maturity: {account_investments['next_bond_maturity_date']}
Mutual Funds: USD {account_investments['mutual_fund_amount']} ({account_investments['total_funds']} funds)

PAYMENTS
Loan Amount: USD {account_payments['loan_amount']}
PF Contribution: USD {account_payments['provident_fund_contribution']}
Insurance Premium: USD {account_payments['insurance_premium']}
"""

        return message
        # return {
        #     "connected_account": account_balance['connected_accounts'],
        #     "account_balance": account_balance['total_account_balance'],
        #     "total_transactions": account_transactions['total_transactions'],
        #     "debit_transaction_amount": account_transactions['debit_transactions_amount'],
        #     "credit_transaction_amount": account_transactions['credit_transactions_amount'],
        #     "upi_transactions_amount": account_transactions['upi_transactions_amount']
        # }