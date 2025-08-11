import requests
from requests.exceptions import HTTPError
import json
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
SEARCH_TERMS = [
    "adobe -\"Adobe Mountain\"", 
    "adobe -\"Adobe style\"",
    "adobe -\"Adobe Style\"", 
    "adobe -\"Adobe-style\"", 
    "adobe -\"Adobe-Style\"", 
    "adobe -\"Adobe home\""
    ]
DATE_RESTRICTION = "d1" #restricts results to last 24 hours
MAX_RESULTS = 100 #100 results per query is max for free tier of API

def run_search(query):
    """Fetch paginated results from Google Custom Search API"""
    results = []
    for start_index in range(1, MAX_RESULTS + 1, 10):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "fields": "items(title,link,displayLink,snippet)",
            "q": query,
            "start": start_index,
            "sort": "date",
            "dateRestrict": DATE_RESTRICTION
        }
        r = requests.get(url, params=params)
        r.raise_for_status() #use try-except logic to handle errors here rather than main?
        data = r.json()
        items = data.get("items", [])
        if not items:
            break
        results.extend(items)
    return results

def main():
    all_new_results = {}

    for query in SEARCH_TERMS:
        try:
            all_new_results[query] = run_search(query)
        except HTTPError as err:
            if err.response.status_code == 429: # Too Many Requests, CSE limits to 100 queries per day
                print(f"Too many requests, skipping query '{query}'. Please try again tomorrow.")
            else:
                print(f"HTTP error {err.response.status_code} with query '{query}': {err}")
        except Exception as e:
            print(f"Error with query '{query}': {e}")

    if all_new_results:
        print(json.dumps(all_new_results, indent = 4))
        print(f"Found {sum(len(items) for items in all_new_results.values())} new results.")
    else:
        print("No new results found.")

if __name__ == "__main__":
    print("running!")
    main()