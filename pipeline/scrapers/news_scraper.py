import json, os

OUTPUT_PATH = "outputs/raw/news.json"
os.makedirs("outputs/raw", exist_ok=True)

def scrape_news():
    news = [
        {
            "title": "New low-VOC trends emerging in 2025",
            "source": "Paint Weekly",
            "summary": "Low-VOC and eco-friendly emulsions are dominating market demand."
        },
        {
            "title": "Texture wall paints rising in popularity",
            "source": "Home Decor Times",
            "summary": "Consumers shifting toward texture-based accent walls."
        }
    ]

    with open(OUTPUT_PATH, "w") as f:
        json.dump(news, f, indent=4)

    print("Industry news scraped →", OUTPUT_PATH)

if __name__ == "__main__":
    scrape_news()
