# Project Documentation — Phishing Awareness Analysis
**DecodeLabs Cybersecurity Training | Project 3 | Batch 2026**

## 1. Objective
The objective of Project 3 is to build the analytical foundation for cybersecurity work by learning to identify phishing attempts through pure threat analysis — no firewalls, no code, no automated tooling. The task simulates the "detection phase" of a Cybersecurity Analyst role: dissecting communication to spot deceptive tactics and malicious intent before any technical defense is implemented.

## 2. Background & Motivation
Phishing remains the leading vector for security breaches:
- Roughly 80% of security breaches involve a phishing component.
- In controlled red-team simulations, around 40% of employees fall for a simulated phishing or vishing attempt.
- Attackers can get their first click in under 90 seconds of a campaign launching.
- Real-world incidents (e.g., the Quanta Computer spear-phishing case, in which a single attacker stole over $100 million from Google and Facebook by spoofing a trusted supplier's domain) show that sophisticated impersonation can bypass even well-resourced organizations.

This confirms that technical controls alone (firewalls, spam filters) are insufficient — the **human firewall** (the end user's judgment) is the last and most important line of defense.

## 3. Scope of Work
Per the project brief, the deliverable required:
1. Identification of suspicious links or keywords in sample messages.
2. A list of red flags found in phishing messages.
3. An explanation of why each message is unsafe.

To make this actionable rather than purely descriptive, the deliverable was structured as a **reusable toolkit**: a checklist + decision tree + worked examples, rather than a one-off analysis.

## 4. Methodology

### 4.1 Threat Taxonomy Reviewed
Before building the checklist, the following attack categories were studied to ensure the checklist covers the full threat surface:
- **Targeting hierarchy:** Mass phishing → Spear phishing → Whaling
- **Channels beyond email:** Smishing (SMS), Vishing (voice), Quishing (QR codes), Search engine phishing (SEO poisoning)
- **Technical disguises:** Display-name spoofing vs. true domain spoofing, typosquatting, homoglyph attacks, combosquatting, subdomain traps, dangling DNS takeovers
- **Psychological triggers:** Authority, urgency, curiosity, fear/greed

### 4.2 Red Flags Catalogued
Eleven categories of red flags were reviewed and consolidated into five practical checklist sections:
1. Sender & domain verification
2. Link & URL inspection
3. Urgency, authority & emotional triggers
4. Attachments & file types
5. Requests for sensitive info or process bypass

### 4.3 Decision Framework
A three-tier classification model was adopted, matching industry-standard triage practice:

| Tier | Meaning | Action |
|---|---|---|
| Safe | No credible indicators of compromise | Close |
| Suspicious | One or more soft/ambiguous red flags | Warn User |
| Malicious | Confirmed spoofing, harvesting, or bypass request | Block & Escalate |

This ensures every triage event ends in a **definitive, actionable outcome** rather than an ambiguous "just be careful."

### 4.4 Worked Examples
Three realistic (fictional) sample messages were authored to demonstrate the toolkit in practice, chosen to represent increasing subtlety:

| # | Type | Key Technique | Classification |
|---|---|---|---|
| 1 | Mass phishing | Homoglyph domain spoof + urgency | Malicious |
| 2 | Spear phishing / BEC | Executive impersonation + secrecy + bypass request | Malicious |
| 3 | Suspicious internal notice | Plausible-but-unverified sender + credential prompt via attachment | Suspicious |

Each example includes the raw message, an itemized list of red flags, and the resulting classification with reasoning — directly satisfying the three project requirements (identify links/keywords, list red flags, explain why it's unsafe).

## 5. Deliverable
**File:** `Project3_Phishing_Triage_Toolkit.docx`

Structure:
1. Purpose
2. Phishing Triage Checklist (5 sections)
3. Decision Tree (classification table)
4. Worked Examples (3 annotated samples)
5. Reporting Reminder

## 6. Key Takeaways
- Phishing exploits the gap between a technical control and a human reaction — the checklist is designed to close that gap for a non-expert.
- Reporting (not just deleting or ignoring) a suspicious message is essential, since it allows a security team to purge the same threat from other inboxes.
- Realistic red flags are often subtle (a single mismatched domain character, a slightly-off sender) rather than obvious, which is why the "Suspicious" tier exists as a middle ground.

## 7. Tools Used
- Manual analysis and documentation (no code required)
- Microsoft Word (.docx) for the final deliverable

## 8. Status
✅ Complete — ready for submission as the Project 3 milestone.
