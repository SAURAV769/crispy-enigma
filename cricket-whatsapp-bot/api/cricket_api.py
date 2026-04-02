import requests
from config.settings import API_KEY

def get_match():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}"
    data = requests.get(url).json()
    return data["data"][0]
    #