import time

# 🧠 Safe dict access (API crash se bachne ke liye)
def safe_get(data, key, default=None):
    try:
        return data.get(key, default)
    except:
        return default


# 🏏 Score key banane ke liye (spam avoid)
def generate_score_key(score):
    try:
        runs = score.get("r", 0)
        wickets = score.get("w", 0)
        overs = score.get("o", 0)
        return f"{runs}-{wickets}-{overs}"
    except:
        return "0-0-0"


# ⏱️ Overs ko float me convert (e.g. 15.3 overs)
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
    overs_float = overs_to_float(overs)
    return overs_float >= (total_overs - 5)


# 🔔 Smart sleep (fast update end me)
def get_sleep_time(overs):
    if is_last_5_overs(overs):
        return 10   # fast update
    return 60       # normal update


# 📈 Required Run Rate calculate
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


# 🔴 Wicket detect
def is_wicket_fallen(prev_wickets, current_wickets):
    try:
        return current_wickets > prev_wickets
    except:
        return False


# ⏳ Delay helper (safe sleep)
def wait(seconds):
    try:
        time.sleep(seconds)
    except:
        pass