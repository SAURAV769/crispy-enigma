from utils.helpers import calculate_rrr, overs_to_float

def format_message(match):
    try:
        teams = match.get("teams", ["Team A", "Team B"])
        score_data = match.get("score", [{}])

        if not score_data:
            return "⚠️ Score not available"

        score = score_data[0]

        runs = score.get("r", 0)
        wickets = score.get("w", 0)
        overs = score.get("o", 0)

        # 🎯 Target (agar available ho)
        target = match.get("target")

        # 📈 Required Run Rate
        rrr = 0
        if target:
            rrr = calculate_rrr(target, runs, overs)

        # 📊 Format message
        msg = f"""
🏏 {teams[0]} vs {teams[1]}

📊 Score: {runs}/{wickets} ({overs} ov)
"""

        if target:
            msg += f"🎯 Target: {target}\n"
            msg += f"📈 Required RR: {rrr}\n"

        return msg

    except Exception as e:
        return f"❌ Error formatting match: {e}"