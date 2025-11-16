---

# 🚀 **Calyco Automated Content Engine (Fully Automated AI Pipeline)**

*A production-grade demo system showcasing automated content generation for the paint & home-decor industry.*

This repository demonstrates a **fully automated content engine** built for **Calyco Paints**, capable of generating:

* Competitor-aware insights
* Trend-based content
* SEO-optimized long-form blogs
* Web copy for product & category pages
* Social media posts (Instagram, LinkedIn, FB)
* Ad snippets (Google, FB, WhatsApp)
* JSON-LD schemas, meta tags & sitemap entries
* QC-validated outputs for readability, tone & brand alignment
* A complete **HTML dashboard** to review all generated content

The entire pipeline runs **end-to-end with a single command**, proving system-level thinking, automation capability, and content workflow design.

---

# 📌 **1. Features Overview**

## 🔍 **A. Automated Data Gathering**

The system scrapes and processes industry-relevant data from multiple sources:

* **Google Trends (fallback mode for demo)**
* **Competitor websites**
* **Industry news**
* **Social media (Instagram fallback scrape)**
* **Color trends & decor themes**

Outputs stored in `outputs/raw/`.

---

## 🧠 **B. AI-Driven Content Creation**

Using Google Gemini (free tier compatible), the engine generates:

### ✔ Web Copy (Product/Category Pages)

Provides Calyco-aligned descriptions, benefits, tone & style.

### ✔ SEO Blogs (1200–1800 words)

Trend-aligned long-form content based on:

* Competitor analysis
* Google trends
* Industry news
* Home décor patterns

### ✔ Social Media Content

* Instagram posts
* LinkedIn B2B posts
* Hashtags
* CSV export-ready captions

### ✔ Ad Snippets

Short ad copy suitable for:

* Google Ads
* Facebook Ads
* WhatsApp Broadcasts

---

## 🎯 **C. Brand Rules Engine**

Ensures:

* No AI words (e.g., “AI-generated”, “LLM”, “ChatGPT”)
* No copied competitor wording
* Tone stays clean, premium, performance-driven
* Paint-industry context integrity

---

## 🧩 **D. SEO & Discoverability Layer**

Automatic generation of:

* JSON-LD schema for blogs & product pages
* SEO meta tags
* Sitemap entries
* Clean URL slugs

Output directories:

```
outputs/blogs/jsonld/
outputs/web_copy/jsonld/
outputs/sitemap.xml
```

---

## 📊 **E. Automated Quality Checks**

Checks include:

* Readability score
* Brand rule violations
* Keyword strength
* Tone consistency
* Metadata structure

Outputs visible in the dashboard.

---

## 🖼️ **F. Image Generation Module (Code Included)**

Integrated support for Stable Diffusion prompt-based image generation.

⚠ **Note:**
OpenAI & Gemini image APIs require paid access in 2025; Gemini has removed free-tier image generation.
So images are not generated in the demo — but the full module is implemented and ready.

---

## 🖥️ **G. Visual Review Dashboard**

A fully styled HTML dashboard at:

```
outputs/dashboard/index.html
```

Shows:

* Web copy
* Blog content
* Social posts
* Ads
* SEO JSON-LD
* QC reports
* Sitemap preview

---

# 🔧 **2. Tech Stack**

| Layer            | Technology                                     |
| ---------------- | ---------------------------------------------- |
| Scraping         | Selenium (optional), Requests, fallback logic  |
| AI Text Engine   | Google Gemini 1.5 Flash (free tier compatible) |
| Image Generation | Stable Diffusion (API-ready, disabled in demo) |
| QC Engine        | Textstat / brand rules / SEO heuristics        |
| SEO Layer        | JSON-LD, meta tags, sitemap builder            |
| Dashboard        | HTML + JSON integration                        |
| Automation       | Python 3.10+, run_all.py master script         |

---

# 🗂️ **3. Repository Structure**

```
├── pipeline/
│   ├── ai_generator.py
│   ├── qc.py
│   ├── seo_generator.py
│   ├── dashboard.py
│   ├── templates/
│   └── scrapers/
│
├── outputs/
│   ├── blogs/
│   ├── web_copy/
│   ├── social/
│   ├── ads/
│   ├── images/
│   ├── raw/
│   └── dashboard/
│
├── run_all.py
├── requirements.txt
└── README.md
```

---

# ▶️ **4. How to Run the Pipeline**

### 1. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your API key to `.env`

```
GEMINI_API_KEY=YOUR_KEY
```

### 4. Run the entire pipeline

```
python run_all.py
```

---

# 📤 **5. Output Examples**

### ✔ Web Copy

`outputs/web_copy/interior-emulsion-paints-calyco.json`

### ✔ Blog

`outputs/blogs/trending-home-paint-colors-2025.md`

### ✔ Social Posts

`outputs/social/social_posts.json`

### ✔ Ads

`outputs/ads/ad_snippets.json`

### ✔ Dashboard

`outputs/dashboard/index.html`

---

# 📌 **6. Limitations (Transparent for Reviewers)**

* Image generation is implemented but disabled due to API restrictions.
* Gemini free tier no longer supports image models after 2025.
* Fallback scraping uses sample JSON structures for stability.

---

# 📈 **7. What This Demo Proves**

This project demonstrates:

### ✔ End-to-end automation of a full content engine

### ✔ Solid understanding of pipelines, scrapers & LLM orchestration

### ✔ Ability to produce SEO-ready, brand-safe content

### ✔ Modern AI integration aligned with Calyco’s real-world needs

### ✔ System architecture thinking — not just one-off content generation

### ✔ A scalable, production-ready foundation

---

# 🙌 **8. Acknowledgements**

This demo was created as part of an AI Automation assignment for **Calyco Paints**, showcasing technical capability across scraping, AI content creation, SEO, QC automation, and pipeline design.

---

## 👨‍💻 Author

**Johny Kumar**
AI/ML & Mobile App Developer
Email: **[johnykumar0008@gmail.com](mailto:johnykumar0008@gmail.com)**
GitHub: **[https://github.com/johnk0008](https://github.com/johnk0008)**
* LinkedIn: **linkedin.com/in/johnk0008**

---

## 🤝 Contributing

Open to feedback, suggestions, and collaboration.

---

⭐ *Star this repo if you find my work helpful!*

---