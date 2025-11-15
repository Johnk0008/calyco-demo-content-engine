🟦 Calyco AI Content Engine 

A modular, automated AI-powered content pipeline for trends → insights → content generation → structured outputs.

---

## 🚀 Overview

This project is a fully functional **AI Content Automation Engine** designed specifically for **Calyco Paints** as part of the demo assignment.

It collects **market trends**, **competitor insights**, and **industry signals**, then automatically generates:

* Product & category **web copy** (JSON)
* Long-form **blogs** (Markdown)
* Social media posts (Instagram & LinkedIn, CSV)
* Ad copy for Google, Facebook & WhatsApp (CSV)

The system is modular, scalable, and easy to extend into a full production-grade content engine.

---

## 🏗️ System Architecture

```
Data Sources
   ├── Google Trends
   ├── Competitor Websites
   ├── Social Feeds
   ├── Industry News
        ↓
Scrapers (Selenium / Requests)
        ↓
Processing Layer
        ↓
AI Content Engine (Gemini 2.0 Flash)
   ├── Web Copy Templates
   ├── Blog Templates
   ├── Social Templates
   ├── Ad Templates
        ↓
Exports
   ├── JSON
   ├── MDX/Markdown
   ├── CSV
```

A visual diagram is provided in:
📁 `docs/architecture_diagram.md`

---

## 📁 Folder Structure

```
calyco-demo-content-engine/
│
├── scrapers/
│   ├── google_trends_scraper.py
│   ├── competitor_scraper.py
│   └── news_scraper.py
│
├── pipeline/
│   ├── process_data.py
│   ├── ai_generator.py
│   ├── exporter.py
│   └── templates/
│       ├── web_copy_template.txt
│       ├── blog_template.txt
│       ├── social_posts_template.txt
│       └── ad_template.txt
│
├── outputs/
│   ├── raw/
│   ├── web_copy/
│   ├── blogs/
│   ├── social/
│   └── ads/
│
├── run_all.py
└── README.md
```

---

## 🔧 Tech Stack

**Languages:** Python
**Automation:** Selenium / Requests
**AI Model:** Gemini 2.0 Flash (FREE)
**Data Output:** JSON, CSV, Markdown
**Environment:** Python 3.11+, Virtualenv

---

## ⚙️ Setup Instructions

### 1️⃣ Install packages

```
pip install -r requirements.txt
```

### 2️⃣ Add your Gemini API key

Create `.env`:

```
GEMINI_API_KEY=YOUR_KEY_HERE
GEMINI_MODEL=gemini-2.0-flash
```

### 3️⃣ Run Scrapers

```
python scrapers/google_trends_scraper.py
python scrapers/competitor_scraper.py
python scrapers/news_scraper.py
```

### 4️⃣ Run AI Content Engine

```
python pipeline/ai_generator.py
```

### 5️⃣ Run Complete Pipeline

```
python run_all.py
```

---

## 🧠 Features Delivered

### ✔ Trend-Aware Content Engine

Integrates Google Trends + industry signals → feeds into LLM templates.

### ✔ Competitor Monitoring

Scrapes insights from pages like:
Asian Paints, Berger, Dulux, Lick, Birla Opus, Indigo Paints.

### ✔ Web Copy Generator

Structured JSON for product/category pages.

### ✔ Blog Generator

1200–1800 word blog drafts in Markdown.

### ✔ Social Media Generator

Instagram + LinkedIn post ideas with hashtags (CSV).

### ✔ Ads Generator

Google Ads, Facebook Ads, WhatsApp hooks (CSV).

### ✔ Modular, Extensible System

Each part can scale independently.

---

## 📦 Output Examples

📁 `/outputs/web_copy/`

* JSON-formatted web copy

📁 `/outputs/blogs/`

* SEO-friendly long-form articles (Markdown)

📁 `/outputs/social/`

* CSV social posts + captions

📁 `/outputs/ads/`

* Ads in CSV format

---

## 🎥 Demo Walkthrough Video

A complete 8–10 minute walkthrough script is available here:
📁 `docs/video_script.md`

The script includes:

* Overview
* Scraper demonstration
* Content engine run
* Architecture explanation
* Closing summary

---

## 🧩 Design Principles

* **Modularity** – every module can scale independently
* **Extensibility** – easy to add new templates or data sources
* **Brand Safety** – no AI mentions; clean and consistent tone
* **Automation Ready** – outputs designed for pipelines (JSON/CSV/MDX)
* **Repeatability** – full content engine, not one-off scripts

---

## 🔮 Future Enhancements

* Better competitor scraping via Playwright
* Automated QC gates with content scoring
* Auto-publishing to CMS platforms
* Vector similarity search for topic clustering
* Multi-language output generation
* Daily/weekly cron scheduling

---

## 👨‍💻 Author

**Johny Kumar**

AI/ML & Mobile App Developer

Email: **[johnykumar0008@gmail.com](mailto:johnykumar0008@gmail.com)**

GitHub: **[https://github.com/johnk0008](https://github.com/johnk0008)**

LinkedIn: **linkedin.com/in/johnk0008**

---

# ⭐ Ready for Calyco Review

This project demonstrates **end-to-end AI automation engineering**:

✔ Trend scraping

✔ Competitor data collection

✔ Structured content generation

✔ Clean exports

✔ Scalable architecture

---

## 🤝 Contributing

Open to feedback, suggestions, and collaboration.

---

⭐ *Star this repo if you find my work helpful!*
