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

def check_wicket(match_id, current_w):
    state = load_state()
    
    prev_w = state.get(f"{match_id}_w", 0)
    
    if current_w > prev_w:
        state[f"{match_id}_w"] = current_w
        save_state(state)
        return True
    
    state[f"{match_id}_w"] = current_w
    save_state(state)
    return False