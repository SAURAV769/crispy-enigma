from twilio.rest import Client #
from config.settings import *

client = Client(TWILIO_SID, TWILIO_TOKEN)

def send_message(msg):
    client.messages.create(
        from_='whatsapp:+14155238886',
        body=msg,
        to=TO_NUMBER
    )