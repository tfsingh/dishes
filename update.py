import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
twilio_sender = os.environ['TWILIO_SENDER']
twilio_recipient = os.environ['TWILIO_RECEPIENT']

client = Client(account_sid, auth_token)

def send_message():
    message = client.messages \
                    .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_= twilio_sender,
                        to= twilio_sender
                    )

def update_backend(face_names):
    return False
