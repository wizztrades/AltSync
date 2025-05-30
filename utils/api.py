# utils/api.py
import requests
from config import API_KEY, BASE_URL
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def get_price_series(symbol: str, limit: int = 90):
    url = f"{BASE_URL}/data/v2/histoday"
    params = {
        "fsym": symbol.upper(),
        "tsym": "USD",
        "limit": limit,
        "api_key": API_KEY
    }
    res = requests.get(url, params=params, timeout=10)
    data = res.json()
    if data['Response'] != 'Success':
        raise ValueError(f"Failed to fetch data for {symbol}: {data.get('Message')}")
    return [entry['close'] for entry in data['Data']['Data']]
