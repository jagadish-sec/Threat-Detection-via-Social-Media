# OSINT on Social Media

## What is OSINT?

Open Source Intelligence (OSINT) is the collection and analysis of data from publicly available sources to produce actionable security intelligence.

---

## Key Techniques

### Profile Analysis
- Search usernames across platforms using `Sherlock` or `Maigret`
- Check account creation date and posting history
- Analyze follower/following ratio for bot detection
- Reverse image search profile pictures (Google Images, TinEye, Yandex)

### Content Analysis
- Archive posts before deletion: `archive.today`, Wayback Machine
- Extract EXIF geolocation from images
- Track hashtag and keyword usage patterns
- Identify linguistic fingerprints across accounts

### Network Mapping
- Map relationships between accounts using Maltego
- Identify coordinated inauthentic behavior (same text, same time)
- Build IOC link graphs for campaign attribution

---

## Essential OSINT Tools

| Tool | Use Case | Type |
|------|----------|----- |
| Maltego | Link analysis, visualization | GUI |
| Sherlock | Username across 300+ platforms | CLI |
| Maigret | Advanced username OSINT | CLI |
| SpiderFoot | Automated collection | Web/CLI |
| theHarvester | Email/domain enumeration | CLI |
| OSINT Framework | Curated tool directory | Web |
| Twint | Twitter OSINT (no API) | CLI |
| Instaloader | Instagram data collection | CLI |

---

## Legal & Ethical Boundaries

- Only collect **publicly available** data
- Never scrape in violation of platform Terms of Service
- Do not deanonymize private individuals without legal basis
- Document methodology for reproducibility and accountability
- Comply with GDPR, IT Act 2000 (India), and local privacy laws

---

## References

- [OSINT Framework](https://osintframework.com/)
- [Bellingcat Toolkit](https://www.bellingcat.com/category/resources/how-tos/)
- [Intel Techniques](https://inteltechniques.com/)
- [SANS OSINT Resources](https://www.sans.org/blog/list-of-resource-lists/)
