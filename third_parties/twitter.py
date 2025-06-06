import requests
import os
from dotenv import load_dotenv

load_dotenv()


def scrap_user_twitter(username: str, num_tweets=5, mock: bool = False):
    """scrap twitter profile via username"""

    if mock:
        # mock data
        return {
            "name": "Richard Chen"
        }
        
    else:
        # Get user's last tweets
        url = "https://api.twitterapi.io/twitter/user/last_tweets"
        querystring = {"userName":"midlifesaaser"}
        headers = {"X-API-Key": os.environ["TWITTERIO_API_KEY"]}
        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.text
        

if __name__ == "__main__":
    print(scrap_user_twitter("midlifesaaser", mock=False))
    