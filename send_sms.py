from twilio.rest import Client
import os
from dotenv import load_dotenv
import random

load_dotenv()

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
to_number = os.environ.get("to_number")
twilio_number = os.environ.get("twilio_number")


def send_message(message_options):
    random_message = message_options[random.randint(0, len(message_options) - 1)]
    client.messages.create(to=to_number,
                           from_=twilio_number,
                           body=random_message)
