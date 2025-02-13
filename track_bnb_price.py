import requests
import time

def get_bnb_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["binancecoin"]["usd"]
    else:
        print("Error fetching data:", response.status_code)
        return None

if __name__ == "__main__":
    while True:
        price = get_bnb_price()
        if price:
            print(f"BNB Price: ${price}")
        time.sleep(60)  # Fetch price every 60 seconds
