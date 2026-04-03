import requests
from config.settings import API_KEY

def get_all_matches():
    try:
        url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        # safe return
        return data.get("data", [])
    
    except Exception as e:
        print("API Error:", e)
        return []