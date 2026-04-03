import json

STATE_FILE = "data/state.json" #

def load_state():
    try:
        return json.load(open(STATE_FILE))
    except:
        return {}

def save_state(state):
    json.dump(state, open(STATE_FILE, "w"))

def should_send(match):
    state = load_state()
    
    score = match["score"][0]
    key = f"{score['r']}-{score['w']}-{score['o']}"
    
    if state.get("last_score") != key:
        state["last_score"] = key
        save_state(state)
        return True
    
    return False