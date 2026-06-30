#!/usr/bin/env python3
"""
Social Media Post Scraper for Threat Detection
Author: Jasti Jagadish Babu
Usage: python tools/social_scraper.py
"""

import re
import json
from datetime import datetime


TARGET_KEYWORDS = [
    "free giveaway click here",
    "your account has been compromised",
    "verify your identity now",
    "limited time offer login",
    "claim your prize",
    "dm for details",
    "click here to secure",
    "account suspended",
]


def extract_urls(text):
    """Extract all URLs from text."""
    return re.findall(r"https?://[^\s]+", text)


def scan_post(post_text):
    """Scan a social media post for threat indicators."""
    result = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "post_snippet": post_text[:100] + "..." if len(post_text) > 100 else post_text,
        "urls_found": extract_urls(post_text),
        "keyword_matches": [],
        "threat_level": "LOW",
        "flags": [],
    }

    post_lower = post_text.lower()

    for keyword in TARGET_KEYWORDS:
        if keyword in post_lower:
            result["keyword_matches"].append(keyword)
            result["flags"].append(f"Matched keyword: '{keyword}'")

    if len(result["urls_found"]) > 2:
        result["flags"].append("Multiple URLs in single post")

    score = len(result["keyword_matches"]) + len(result["urls_found"])
    if score >= 4:
        result["threat_level"] = "HIGH"
    elif score >= 2:
        result["threat_level"] = "MEDIUM"

    return result


def scan_file(filepath):
    """Scan posts from a text file separated by blank lines."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()
        posts = [p.strip() for p in raw.split("\n\n") if p.strip()]
        return [scan_post(post) for post in posts]
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return []


if __name__ == "__main__":
    demo_posts = [
        "URGENT: Your account has been compromised! Click here to secure it now: http://verify-account.xyz/login",
        "Free giveaway click here to claim your prize! Limited time only: http://bit.ly/freegift",
        "Good morning! Hope everyone has a productive day ahead.",
    ]

    print("=" * 60)
    print("  Social Media Threat Scanner - Demo Mode")
    print("=" * 60)

    for post in demo_posts:
        result = scan_post(post)
        print(f"\n[{result['threat_level']}] {result['post_snippet']}")
        if result["flags"]:
            for flag in result["flags"]:
                print(f"  ⚠  {flag}")
        if result["urls_found"]:
            print(f"  🔗 URLs: {result['urls_found']}")
