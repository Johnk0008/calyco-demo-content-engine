import pandas as pd
import os

def export_social_posts():
    # Demo CSV
    rows = [
        ["Instagram", "Top texture ideas for 2025", "#home #paint", "2025-11-12"],
        ["LinkedIn", "Low-VOC paints rising demand", "#decor #painting", "2025-11-13"],
    ]
    
    df = pd.DataFrame(rows, columns=["Platform", "Caption", "Hashtags", "Schedule"])

    os.makedirs("outputs/social_posts", exist_ok=True)
    df.to_csv("outputs/social_posts/social_schedule.csv", index=False)

    print("CSV exported → outputs/social_posts/social_schedule.csv")

if __name__ == "__main__":
    export_social_posts()
