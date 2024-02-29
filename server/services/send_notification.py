import os

import boto3

class SendMessage:

    def __init__(self, message):
        self.message = message
        
    def sns_send_message(message):
        sns_client = boto3.client('sns')

        response = sns_client.publish(
            TopicArn=os.getenv("SNS_TOPIC_ARN"),
            Message=message
        )

        print(response['MessageId'])