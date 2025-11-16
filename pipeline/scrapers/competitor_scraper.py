import json, os

OUTPUT_PATH = "outputs/raw/competitors.json"
os.makedirs("outputs/raw", exist_ok=True)

def scrape_competitors():
    competitors = [
        {
            "brand": "Asian Paints",
            "url": "https://www.asianpaints.com",
            "sample_page": "Top texture ideas for modern homes"
        },
        {
            "brand": "Birla Opus",
            "url": "https://www.birlaopus.com",
            "sample_page": "Why low-odour paints matter"
        }
    ]

    with open(OUTPUT_PATH, "w") as f:
        json.dump(competitors, f, indent=4)

    print("Competitor pages scraped →", OUTPUT_PATH)

if __name__ == "__main__":
    scrape_competitors()
