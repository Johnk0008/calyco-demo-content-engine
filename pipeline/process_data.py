import json

def load_raw_data():
    with open("outputs/raw/google_trends.json") as f1:
        trends = json.load(f1)

    with open("outputs/raw/news.json") as f2:
        news = json.load(f2)

    with open("outputs/raw/competitor_pages.json") as f3:
        competitors = json.load(f3)

    return {
        "trends": trends,
        "news": news,
        "competitors": competitors
    }

if __name__ == "__main__":
    data = load_raw_data()
    print("Loaded all raw data successfully.")
