# pipeline/__init__.py
"""
Pipeline package exports
Ensures run_all.py can import functions cleanly.
"""

# --- Import scrapers ---
from .scrapers.trends_scraper import scrape_google_trends
from .scrapers.news_scraper import scrape_news
from .scrapers.competitor_scraper import scrape_competitors
from .scrapers.social_scraper import scrape_instagram_profile

# --- Import AI generators ---
from .ai_generator import (
    generate_web_copy,
    generate_blog,
    generate_social_posts,
    generate_ads,
)

# --- Import QC ---
from .qc import run_quality_checks

__all__ = [
    "scrape_google_trends",
    "scrape_news",
    "scrape_competitors",
    "scrape_instagram_profile",
    "generate_web_copy",
    "generate_blog",
    "generate_social_posts",
    "generate_ads",
    "run_quality_checks",
]
