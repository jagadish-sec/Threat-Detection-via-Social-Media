# Threat Report: Twitter Phishing Campaign

**Report ID:** THREAT-20260630-001  
**Date:** 2026-06-30  
**Analyst:** Jasti Jagadish Babu  
**Platform:** Twitter (X)  
**Severity:** HIGH  
**Status:** Documented  

---

## Executive Summary

A phishing campaign was detected on Twitter (X) using fake "account verification" messages directing users to a credential harvesting page mimicking PayPal's login portal. The campaign used a typosquatted domain and urgency-based social engineering.

---

## Threat Indicators (IOCs)

| Indicator | Type | Description |
|-----------|------|-------------|
| `http://paypa1-verify.xyz/login` | Malicious URL | Typosquatted PayPal domain |
| `@PayPa1_Support` | Fake Account | Impersonating PayPal support |
| "Your account is suspended" | Phishing Phrase | Urgency-based social engineering |
| `185.220.101.xx` | IP Address | Bulletproof hosting provider |

---

## Attack Chain

1. **Initial Contact** — Victim receives unsolicited DM from `@PayPa1_Support`
2. **Urgency Trigger** — Message claims account will be permanently suspended in 24hrs
3. **Redirect** — Shortened URL leads to `paypa1-verify.xyz/login`
4. **Credential Harvest** — Fake login page captures username and password
5. **Account Takeover** — Attacker accesses victim's real PayPal account

---

## OSINT Findings

- Domain `paypa1-verify.xyz` registered 3 days before campaign start
- Hosting: Bulletproof provider in Eastern Europe
- SSL: Let's Encrypt (auto-renewed every 30 days)
- Related domains: `paypa1-help.com`, `paypa1-secure.net`
- Fake account `@PayPa1_Support` created 5 days prior, 0 followers

---

## Recommended Actions

- [ ] Report `@PayPa1_Support` to Twitter Trust & Safety
- [ ] Submit `paypa1-verify.xyz` to PhishTank and VirusTotal
- [ ] Alert PayPal security team with full IOC list
- [ ] Notify users who interacted with the fake account

---

## MITRE ATT&CK Mapping

| Technique | ID | Tactic |
|-----------|-----|--------|
| Spearphishing via Social Media | T1566.003 | Initial Access |
| Credential Phishing | T1056 | Collection |
| Impersonation | T1656 | Defense Evasion |
| Web Service (social media C2) | T1102 | Command & Control |

---

*This report is for educational and ethical research purposes only.*
