# Case Studies: Real-World Social Media Threats

---

## Case 1: Twitter Crypto Scam — Bitcoin Giveaway

**Type:** Financial Scam  
**Platform:** Twitter  
**Severity:** HIGH  
**Year:** 2020  

### What Happened
Attackers compromised high-profile verified accounts and posted fake Bitcoin giveaway messages claiming users would receive double their sent BTC.

### TTPs Used
- Account takeover via SIM swapping and phishing
- Authority exploitation (impersonating public figures)
- Cryptocurrency irreversibility as a fraud enabler

### Detection Signals
- Sudden change in account posting behavior
- Posts containing crypto wallet addresses
- Urgency language: "limited time", "act now"

### Lessons Learned
- Enable hardware 2FA (YubiKey) on high-value accounts
- Verify all crypto offers via official channels — not social media
- Platforms should flag sudden behavioral changes on verified accounts

---

## Case 2: LinkedIn Spearphishing — Fake Recruiter

**Type:** Spearphishing  
**Platform:** LinkedIn  
**Severity:** CRITICAL  
**Year:** 2022  

### What Happened
North Korea-linked Lazarus Group created convincing fake recruiter profiles targeting aerospace and defense professionals with malicious job offer PDFs.

### TTPs Used
- T1566.002 — Spearphishing via attachment
- Fake job lure social engineering
- Macro-embedded PDF delivering backdoor malware

### Detection Signals
- Recruiter profile recently created
- Company name doesn't match official hiring channels
- Unsolicited PDF attachment in first message

### Lessons Learned
- Verify recruiter identities via official company websites
- Disable macros in Office applications by default
- Use endpoint detection tools (EDR) on work machines

---

## Case 3: Instagram Phishing via DM

**Type:** Credential Phishing  
**Platform:** Instagram  
**Severity:** MEDIUM  

### What Happened
Fake "Instagram Security" accounts mass-DM'd users warning their accounts would be deleted unless they verified via an external link — which harvested Instagram credentials.

### IOCs
- Domain: `instagram-security-verify.com`
- Fake account: `@Instagram_Security_Help`
- Keyword: "your account will be permanently deleted"

### Detection Method
- Regex match on "account will be deleted" + external URL
- Domain WHOIS: registered 2 days before campaign
- Account age: 4 days, 0 posts, 0 followers

### Lessons Learned
- Instagram will never DM you from an unverified account
- Check domain age before clicking any verification link
- Report fake accounts using the in-app report feature

---

## Key Takeaways Across All Cases

1. Urgency, authority, and fear are the attacker's primary weapons
2. New accounts + suspicious domains are strong early warning signals
3. URL shorteners and typosquatted domains are common evasion tactics
4. OSINT on domain registration can expose campaigns within hours
5. Always verify requests via official channels — never through a DM or link
