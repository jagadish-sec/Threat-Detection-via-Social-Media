#!/usr/bin/env python3
"""
Threat Classifier for Social Media Intelligence
Author: Jasti Jagadish Babu
Usage: python tools/threat_classifier.py
"""

import json
from datetime import datetime


THREAT_RULES = {
    "PHISHING": {
        "keywords": ["verify", "login", "password", "suspended", "click here", "confirm"],
        "severity": "HIGH",
        "action": "Report to platform + block domain + alert affected users",
    },
    "MALWARE_DISTRIBUTION": {
        "keywords": ["download", "crack", "keygen", "free software", ".exe", ".apk", "torrent"],
        "severity": "CRITICAL",
        "action": "Submit to VirusTotal + notify CERT-In + document IOCs",
    },
    "SCAM": {
        "keywords": ["giveaway", "free money", "prize", "you won", "gift card", "bitcoin double"],
        "severity": "MEDIUM",
        "action": "Report to platform abuse team + document the account",
    },
    "IMPERSONATION": {
        "keywords": ["official account", "support team", "we are the admin", "from the team"],
        "severity": "HIGH",
        "action": "Report fake account + alert the impersonated organization",
    },
    "DOXXING": {
        "keywords": ["home address", "phone number", "personal info leaked", "exposed", "dox"],
        "severity": "CRITICAL",
        "action": "Immediate report + notify victim + consider legal action",
    },
}

SEVERITY_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}


def classify(post_text, platform="Unknown"):
    """Classify a social media post into a threat category."""
    text_lower = post_text.lower()
    best_type = "UNCLASSIFIED"
    best_severity = "LOW"
    best_hits = []
    best_action = "Monitor and document for further analysis"

    for threat_type, rules in THREAT_RULES.items():
        hits = [kw for kw in rules["keywords"] if kw in text_lower]
        if hits and SEVERITY_RANK[rules["severity"]] >= SEVERITY_RANK[best_severity]:
            best_type = threat_type
            best_severity = rules["severity"]
            best_hits = hits
            best_action = rules["action"]

    return {
        "id": f"THREAT-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "platform": platform,
        "threat_type": best_type,
        "severity": best_severity,
        "indicators": best_hits,
        "recommended_action": best_action,
        "content_snippet": post_text[:120],
    }


if __name__ == "__main__":
    test_cases = [
        ("Your PayPal account is suspended. Login here to verify: http://paypal-verify.xyz", "Twitter"),
        ("Download FREE Photoshop crack! Get the .exe keygen now via this link!", "Telegram"),
        ("FREE Bitcoin giveaway! Send 0.01 BTC and get 0.1 BTC back — bitcoin double!", "Instagram"),
        ("We are the admin team. Your account needs review. DM us your credentials.", "Facebook"),
    ]

    print("=" * 60)
    print("  Threat Classifier - Demo Mode")
    print("=" * 60)

    for text, platform in test_cases:
        r = classify(text, platform)
        print(f"\n[{r['severity']}] {r['threat_type']} | {platform}")
        print(f"  ID: {r['id']}")
        print(f"  Indicators: {r['indicators']}")
        print(f"  Action: {r['recommended_action']}")
