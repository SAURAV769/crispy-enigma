import time

# 🧠 Safe dict access
def safe_get(data, key, default=None):
    if isinstance(data, dict):
        return data.get(key, default)
    return default


# 🏏 Score key (spam avoid)
def generate_score_key(score):
    if not isinstance(score, dict):
        return "0-0-0"
    
    runs = score.get("r", 0)
    wickets = score.get("w", 0)
    overs = score.get("o", 0)
    
    return f"{runs}-{wickets}-{overs}"


# ⏱️ Overs → float (15.3 → 15.5)
def overs_to_float(overs):
    try:
        overs = float(overs)
        full_overs = int(overs)
        balls = int((overs - full_overs) * 10)
        return full_overs + (balls / 6)
    except:
        return 0.0


# ⚡ Last 5 overs check
def is_last_5_overs(overs, total_overs=20):
    return overs_to_float(overs) >= (total_overs - 5)


# 🔔 Smart sleep (⚡ fast end overs)
def get_sleep_time(overs):
    return 10 if is_last_5_overs(overs) else 60


# 📈 Required Run Rate
def calculate_rrr(target, current_runs, overs_done, total_overs=20):
    try:
        overs_float = overs_to_float(overs_done)
        balls_left = (total_overs - overs_float) * 6
        runs_needed = target - current_runs

        if balls_left <= 0 or runs_needed <= 0:
            return 0.0

        return round((runs_needed / balls_left) * 6, 2)
    except:
        return 0.0


# 🔴 Wicket detect (simple)
def is_wicket_fallen(prev_wickets, current_wickets):
    return current_wickets > prev_wickets


# ⏳ Safe sleep
def wait(seconds):
    time.sleep(seconds)