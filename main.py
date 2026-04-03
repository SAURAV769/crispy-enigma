from api.cricket_api import get_all_matches
from services.whatsapp import send_message
from services.notifier import should_send, check_wicket
from utils.helpers import generate_score_key, get_sleep_time, wait
from utils.formatter import format_message
from config.settings import validate_settings
import http.server
import socketserver
import threading

print("🚀 Bot started...")

while True:
    print("🔄 Checking matches...")
    matches = get_all_matches()

send_message("🔥 Test Message - Bot Active")
def start_server():
    PORT = 10000
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("🌐 Server running on port", PORT)
        httpd.serve_forever()

# server ko background me chalao
threading.Thread(target=start_server, daemon=True).start()


validate_settings()

while True:
    matches = get_all_matches()

    for match in matches:
        match_id = match.get("id")

        score_data = match.get("score", [{}])
        if not score_data:
            continue

        score = score_data[0]

        runs = score.get("r", 0)
        wickets = score.get("w", 0)
        overs = score.get("o", 0)

        # 🧠 Unique score key
        score_key = generate_score_key(score)

        # 📊 Format message
        message = format_message(match)

        # 🔴 Wicket alert
        if check_wicket(match_id, wickets):
            send_message("🔴 WICKET ALERT!\n" + message)

        # 🚫 Spam control
        elif should_send(match_id, score_key):
            send_message(message)

    # ⚡ Smart delay
    wait(30)
