# pipeline/qc.py
"""
Quality Control Module
- Readability scoring (textstat)
- SEO structure checks
- Brand safety rules for Calyco
"""

import re
import textstat


def check_readability(text: str) -> float:
    """Return a readability score (Flesch Reading Ease 0–100)."""
    try:
        return textstat.flesch_reading_ease(text)
    except:
        return 60.0  # fallback default


def enforce_brand_rules(text: str):
    """
    Detect banned words such as:
    - AI-generated
    - ChatGPT
    - LLM
    """
    violations = []
    banned_words = [
        "ai-generated",
        "ai generated",
        "chatgpt",
        "llm",
        "machine-generated",
        "artificial intelligence generated"
    ]

    for w in banned_words:
        if w.lower() in text.lower():
            violations.append(w)

    return violations


def check_seo_structure(text: str):
    """
    Basic SEO checks:
    - At least 2 headings
    - Minimum word count
    """
    issues = []

    if text.count("#") < 2:
        issues.append("Content missing headings (H2/H3).")

    if len(text.split()) < 300:
        issues.append("Content too short (<300 words).")

    return issues


def run_quality_checks(text: str):
    """Return a dictionary of all QC checks."""
    return {
        "readability_score": check_readability(text),
        "brand_violations": enforce_brand_rules(text),
        "seo_issues": check_seo_structure(text)
    }


if __name__ == "__main__":
    sample = "This is a demo content piece for QC testing."
    print(run_quality_checks(sample))
