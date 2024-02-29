# FinApp
**[PROOF OF CONCEPT]**

Get daily notification updates about your personal finances. A platform which is connected to your bank account(s) to provide you with financial insights paired with a bot to send you notifications on the go. Helps you to keep a track of your expenses and also manage your investments, payments and **unnecessary spendings**.

### Features
 - Receive daily personal financial updates
 - Get updated with recent expenses and transactions
 - Connect multiple accounts with different banks and receive unified updates

## Installation
**Clone the Repo**

    $ https://github.com/Dhirajjjj/FinApp.git
    $ cd finapp

**Create and run Virtual enviornment**

    $ python -m venv venv
    $ . \venv\Scripts\activate

**Install dependencies**

    $ pip install -r requirements.txt

### Backend  Setup 
The Backend provides a REST API endpoint server to fetch financial data using the Django Rest Framework. This server provides the bot with sample financial data which can be replaced with respective bank's developer APIs. This step is optional.

Ensure that django and its dependencies have been setup

    $ cd backend
**Make migrations**

    $ python manage.py makemigrations
    $ python manage.py migrate
**Create superuser and run server**

    $ python manage.py createsuperuser
    $ python manage.py runserver 8000

Once completed feed the backend with sample data which can be done by

    $ python feed.py

### AWS SNS Setup
The notifications are currently handled by simple notification service

> Login to your aws account
> Create new sns topic
> Create subscriptions for the aforementioned topic

**AWS CLI**
configure aws and setup the following environment variables

    $ aws configure
    AWS Access Key ID: MYACCESSKEY
    AWS Secret Access Key: MYSECRETKEY
    Default region name [us-west-2]: us-west-2
    $ export AWS_ACCESS_KEY_ID=<access_key>
    $ export AWS_SECRET_ACCESS_KEY=<secret_key>

Now you are good to go!

    $ python server/main.py

Start with this to receive your first update on finances

## There's more to come

![Screenshot_20240229_152908_Messages](https://github.com/Dhirajjjj/FinApp/assets/69754979/59c91a78-f97f-4d66-b85b-b0e2cd5652d1)
