import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 API
API_KEY = os.getenv("API_KEY")

# 📲 WhatsApp
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TO_NUMBER = os.getenv("TO_NUMBER")
FROM_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox


# ⚠️ Validation (important)
def validate_settings():
    missing = []

    if not API_KEY:
        missing.append("API_KEY")
    if not TWILIO_SID:
        missing.append("TWILIO_SID")
    if not TWILIO_TOKEN:
        missing.append("TWILIO_TOKEN")
    if not TO_NUMBER:
        missing.append("TO_NUMBER")

    if missing:
        raise Exception(f"❌ Missing environment variables: {', '.join(missing)}")