import os
from dotenv import load_dotenv

from services.send_notification import SendMessage
from services.account_summary import AccountSummary

def main():
    summary = AccountSummary()
    message = summary.generate_summary()
    print(message)
    # SendMessage.sns_send_message(message)

if __name__ == '__main__':
    load_dotenv()
    main()

"""
    Next Steps:
        1. Create DB <- postgresql [DONE]
            a. Account
                1. Balance [DONE]
                2. Investments [DONE] 
                    a. FDs
                    b. Stocks
                    c. Bonds
                    d. Mutual Funds
                3. Payments [SKIP]
                    a. Loan
                    b. PPF
                    c. SIP
            b. Transactions
        2. Flask API server [DONE] (Used Django instead)
            a. Get balance
            b. Get transactions last 30 days
            c. Get transactions current month
            d. Get investments
            e. Get previous days transactions   
        3. Feed Sample data [DONE]
        4. Create insights / Draft a message - [check with plaid]
"""

"""
    1. Setup AWS SNS service
    2. Configure AWS CLI
    3. Setup project
"""