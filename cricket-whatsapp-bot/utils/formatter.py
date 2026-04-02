def format_msg(match):
    score = match["score"][0]
    
    runs = score["r"]
    wickets = score["w"]
    overs = score["o"]
    
    return f"Score: {runs}/{wickets} ({overs})"