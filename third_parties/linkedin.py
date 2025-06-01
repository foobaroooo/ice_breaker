import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrap_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrap linked profile via url"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/foobaroooo/ed39eb73ab4e7ca6fd8b81c24ba01b69/raw/82bad38c70291f5cd68758901e2a664087c0b91b/langchain_linkedin_scraping.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }

        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")

    # remove blank and certifications data (also blank)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrap_linkedin_profile("https://www.linkedin.com/in/michael-huang-006a1017/", True)
    )
