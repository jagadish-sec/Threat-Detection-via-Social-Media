# 🔍 Threat Detection via Social Media

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Security](https://img.shields.io/badge/Focus-Threat%20Detection-red?style=flat-square)
![OSINT](https://img.shields.io/badge/Type-OSINT-green?style=flat-square)

A cybersecurity project focused on identifying threats, scams, phishing, and malicious activity originating from social media platforms using Python-based tools and OSINT techniques.

---

## 📁 Project Structure

```
Threat-Detection-via-Social-Media/
├── README.md
├── requirements.txt
├── src/
│   ├── social_scraper.py       # Scans post text for threat indicators
│   ├── keyword_analyzer.py     # Regex-based phishing pattern detection
│   └── threat_classifier.py   # Classifies threat type + severity
├── indicators/
│   ├── phishing_keywords.txt   # Keyword watchlist
│   ├── malicious_domains.txt   # Known bad domain patterns
│   └── suspicious_patterns.txt # Behavioral red flags
├── reports/
│   ├── sample_threat_report.md # Example report with MITRE ATT&CK mapping
│   └── analysis_template.md   # Blank template for future reports
└── notes/
    ├── OSINT_Social_Media.md   # OSINT tools and techniques
    ├── Threat_Intelligence.md  # TI lifecycle, IOC types
    └── Case_Studies.md        # Real-world threat case studies
```

---

## 🎯 Objectives

- Monitor social media content for threat indicators
- Identify phishing links, scam accounts, and malware distribution
- Perform OSINT on suspicious profiles and domains
- Classify threats by type and severity (LOW / MEDIUM / HIGH / CRITICAL)
- Generate structured, actionable threat reports

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core scripting |
| `requests` | HTTP requests |
| `re` (regex) | Pattern matching |
| `beautifulsoup4` | HTML parsing |
| VirusTotal API | URL/domain reputation |
| Shodan | Infrastructure lookup |
| Maltego | Link analysis |
| Sherlock | Username OSINT |

---

## 🚨 Threat Categories

| Category | Severity | Description |
|----------|----------|-------------|
| Phishing | HIGH | Credential harvesting via fake login pages |
| Malware Distribution | CRITICAL | Malicious files/links shared via DMs |
| Scam | MEDIUM | Fake giveaways, crypto fraud |
| Impersonation | HIGH | Fake brand/support accounts |
| Doxxing | CRITICAL | Personal info leaks |

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Analyze a single post
```bash
python src/keyword_analyzer.py --text "URGENT: Your account has been suspended. Click here to verify!"
```

### 3. Analyze a file of posts
```bash
python src/keyword_analyzer.py --input data/sample_posts.txt
```

### 4. Classify threats from a file
```bash
python src/threat_classifier.py
```

### 5. Run the scraper demo
```bash
python src/social_scraper.py
```

---

## ⚠️ Disclaimer

This project is for **educational and ethical security research only**. Always obtain proper authorization before monitoring any social media account or platform. Comply with platform Terms of Service and applicable local laws (GDPR, IT Act, etc.).

---

## 👤 Author

**Jasti Jagadish Babu**  
CEH | VAPT & Penetration Testing | B.Tech CS & CyberSecurity  
GitHub: [jagadish-sec](https://github.com/jagadish-sec)
