import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
twilio_sender = os.environ['TWILIO_SENDER']
twilio_recipient = os.environ['TWILIO_RECEPIENT']

client = Client(ccount_sid, auth_token)

def send_message(face_names):
    content = " ".join(str(name) for name in face_names) + " added a dish to the sink."

    message = client.messages \
                    .create(
                        body=content,
                        from_= twilio_sender,
                        to= twilio_recipient
                    )


endpoint = os.environ['API_ENDPOINT']

def update_backend(face_names):
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        for name in face_names:
            matching_row = next((row for row in data if row['name'] == name), None)
            if matching_row:
                matching_row['count'] = int(matching_row['count']) + 1
                response = requests.put(f'{endpoint}/name/{matching_row["name"]}', json=matching_row)
                if response.status_code != 200:
                    print(f'Failed to update row for name {matching_row["name"]}')
            else:
                print(f'No row found for name {name}')
    else:
        print('Failed to fetch data from table')
