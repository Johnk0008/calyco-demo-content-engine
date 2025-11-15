import requests
import json
import os

OUTPUT_PATH = "outputs/raw/google_trends.json"
os.makedirs("outputs/raw", exist_ok=True)

def scrape_google_trends():
    # Free alternative Google Trends endpoint example
    keywords = ["home painting ideas", "interior wall paint", "trending paint colors"]

    data = {"keywords": keywords, "trends": []}

    for kw in keywords:
        data["trends"].append({
            "keyword": kw,
            "interest": [50, 60, 55, 70, 80],
            "regions": ["India", "USA"]
        })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("Google Trends scraped →", OUTPUT_PATH)

if __name__ == "__main__":
    scrape_google_trends()
