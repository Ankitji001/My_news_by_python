import os
import requests
from dotenv import load_dotenv

# Load system environment keys (Works from local .env or GitHub Cloud Secrets!)
load_dotenv()

def fetch_live_news():
    # 1. Fetch the full value stored in the environment variable
    full_url = os.getenv('NEWS_API_KEY')
    
    # 2. Pass the fetched variable string into requests (WITHOUT literal quotes)
    response = requests.get(full_url).json()
    
    print("\n=== LIVE NEWS STREAM FROM GITHUB CLOUD ===")
    for index, article in enumerate(response['articles'][:5], 1):
        print(f"{index}. {article['title']}")
        print(f"   Description: {article['description']}\n")

if __name__ == "__main__":
    fetch_live_news()
