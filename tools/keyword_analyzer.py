#!/usr/bin/env python3
"""
Keyword Analyzer for Social Media Threat Detection
Author: Jasti Jagadish Babu
Usage:
  python tools/keyword_analyzer.py --text "Your account is suspended!"
  python tools/keyword_analyzer.py --input data/posts.txt
"""

import re
import json
import argparse


PHISHING_PATTERNS = [
    (r"click here.{0,25}(verify|confirm|update|secure)", "Phishing CTA"),
    (r"your (account|password).{0,20}(suspend|block|comprom|expir)", "Account threat lure"),
    (r"(win|won|prize|reward|gift).{0,30}(claim|collect|free)", "Prize scam"),
    (r"(urgent|immediate).{0,15}action", "Urgency trigger"),
    (r"(login|sign.?in).{0,20}(now|immediately)", "Forced login"),
    (r"(bit\.ly|tinyurl\.com|goo\.gl)/[a-zA-Z0-9]+", "Shortened URL"),
]

SOCIAL_ENG_PATTERNS = [
    (r"dm.{0,15}(detail|info|more)", "DM lure"),
    (r"(only|limited).{0,15}(time|spots|slots)", "False scarcity"),
    (r"guaranteed.{0,15}(free|profit|safe)", "Fake guarantee"),
    (r"send.{0,15}(btc|crypto|bitcoin|gift card)", "Crypto fraud"),
]


def analyze(text):
    """Analyze text for phishing and social engineering patterns."""
    text_lower = text.lower()
    result = {
        "phishing_hits": [],
        "social_engineering_hits": [],
        "risk_score": 0,
        "risk_level": "LOW",
    }

    for pattern, label in PHISHING_PATTERNS:
        if re.search(pattern, text_lower):
            result["phishing_hits"].append(label)
            result["risk_score"] += 2

    for pattern, label in SOCIAL_ENG_PATTERNS:
        if re.search(pattern, text_lower):
            result["social_engineering_hits"].append(label)
            result["risk_score"] += 1

    if result["risk_score"] >= 5:
        result["risk_level"] = "HIGH"
    elif result["risk_score"] >= 2:
        result["risk_level"] = "MEDIUM"

    return result


def analyze_file(filepath):
    """Analyze each line in a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
        flagged = []
        for i, line in enumerate(lines, 1):
            res = analyze(line)
            if res["risk_score"] > 0:
                flagged.append({"line": i, "text": line[:80], **res})
        return flagged
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Social Media Keyword Threat Analyzer")
    parser.add_argument("--text", help="Analyze a single text string")
    parser.add_argument("--input", help="Analyze a text file (one post per line)")
    args = parser.parse_args()

    if args.text:
        print(json.dumps(analyze(args.text), indent=2))
    elif args.input:
        print(json.dumps(analyze_file(args.input), indent=2))
    else:
        demos = [
            "URGENT: Your account will be suspended! Click here to verify now!",
            "Limited time only — DM me for more details on this free offer!",
            "Send 0.1 BTC guaranteed to receive 1 BTC back!",
            "Hey everyone, have a great Tuesday!",
        ]
        print("Demo Analysis Results\n" + "=" * 40)
        for d in demos:
            r = analyze(d)
            print(f"\n[{r['risk_level']}] {d[:60]}")
            if r["phishing_hits"]:
                print(f"  Phishing: {r['phishing_hits']}")
            if r["social_engineering_hits"]:
                print(f"  SocEng:   {r['social_engineering_hits']}")
