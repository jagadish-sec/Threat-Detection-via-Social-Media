# Threat Intelligence

## The Threat Intelligence Lifecycle

1. **Planning** — Define requirements, identify target platforms and threat actors
2. **Collection** — Gather raw data: posts, profiles, URLs, IPs, hashes
3. **Processing** — Parse, normalize, deduplicate raw data
4. **Analysis** — Identify TTPs, IOCs, patterns, and actor attribution
5. **Dissemination** — Share as STIX/TAXII, PDF reports, or platform alerts
6. **Feedback** — Improve collection strategy based on findings

---

## Indicators of Compromise (IOCs)

| IOC Type | Example | Volatility |
|----------|---------|------------|
| IP Address | 185.220.101.x | High |
| Domain | phish-example.com | Medium |
| URL | http://evil.com/login | High |
| File Hash (SHA256) | e3b0c44298fc... | Low |
| Email Address | attacker@evil.com | Medium |
| Username | @FakeSupp0rt | High |
| SSL Certificate | fingerprint hash | Low |

---

## Social Media Threat Actors

| Actor Type | Motivation | Common TTPs |
|------------|-----------|-------------|
| Cybercriminals | Financial | Phishing, scams, fraud |
| Nation-State | Espionage | Spearphishing, disinformation |
| Hacktivists | Ideology | Doxxing, DDoS threats |
| Script Kiddies | Notoriety | Pre-built tools, spam |
| Insider Threats | Revenge/Gain | Data exfiltration via DMs |

---

## MITRE ATT&CK — Social Media Relevant Techniques

| Technique | ID | Description |
|-----------|-----|-------------|
| Spearphishing via Social Media | T1566.003 | Phishing via DMs |
| Impersonation | T1656 | Fake brand/support accounts |
| Search Open Websites | T1593 | Passive OSINT recon |
| Phishing for Information | T1598 | Credential or data harvesting |
| Gather Victim Identity Info | T1589 | Profile enumeration |

---

## Threat Intelligence Feeds

- [PhishTank](https://www.phishtank.com/) — Phishing URL database
- [AbuseIPDB](https://www.abuseipdb.com/) — Malicious IP reports
- [VirusTotal](https://www.virustotal.com/) — URL/file/domain scanning
- [URLhaus](https://urlhaus.abuse.ch/) — Malware URL feed
- [AlienVault OTX](https://otx.alienvault.com/) — Open Threat Exchange
- [MISP](https://www.misp-project.org/) — Threat intelligence platform
