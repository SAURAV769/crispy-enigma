from twilio.rest import Client
from config.settings import TWILIO_SID, TWILIO_TOKEN, TO_NUMBER, FROM_NUMBER

client = Client(TWILIO_SID, TWILIO_TOKEN)

def send_message(msg):
    try:
        message = client.messages.create(
            from_=FROM_NUMBER,   # Twilio sandbox number
            body=msg,
            to=TO_NUMBER
        )
        print("✅ Sent:", message.sid)
    except Exception as e:
        print("❌ WhatsApp Error:", e)
        