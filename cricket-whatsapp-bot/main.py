from api.cricket_api import get_match#
from services.whatsapp import send_message
from services.notifier import should_send
from utils.helpers import *


while True:
    match = get_match()
    
    if should_send(match):
        send_message(match)
        

score_key = generate_score_key(score)

if is_last_5_overs(overs):
    print("Fast mode ON ⚡")

rrr = calculate_rrr(180, 120, 15.2)

sleep_time = get_sleep_time(overs)
wait(sleep_time)