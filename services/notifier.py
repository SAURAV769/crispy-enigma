import json
import os

STATE_FILE = "data/state.json"

# 📂 ensure file exists
def load_state():
    try:
        if not os.path.exists(STATE_FILE):
            return {}
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# 🎯 per match spam control
def should_send(match_id, score_key):
    state = load_state()
    
    last_score = state.get(match_id)
    
    if last_score != score_key:
        state[match_id] = score_key
        save_state(state)
        return True
    
    return False