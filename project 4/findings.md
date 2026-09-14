# Detailed Audit Findings — Project 4

**System:** Lenovo LAPTOP-1QFMA1GS | Windows 11 Home Build 26200  
**Audit Date:** September 13, 2026  
**Auditor:** Sneha Tyagi

---

## Complete Findings Matrix

| # | Audit Step | Finding | Risk Level | Status | Evidence | Remediation |
|---|-----------|---------|-----------|--------|----------|-------------|
| 1 | Identity & Auth | Guest Account | High | ✅ Fixed | Screenshot 3: Disabled | Already disabled before audit |
| 2 | Identity & Auth | Administrator Account | High | ✅ Fixed | Screenshot 3: Disabled | Already disabled before audit |
| 3 | Identity & Auth | Active User (Sneha Tyagi) | Low | ✅ OK | Screenshot 4: Enabled | No action needed |
| 4 | Identity & Auth | Admin Group Members | Low | ✅ OK | Screenshot 5: 2 members | Properly configured |
| 5 | Identity & Auth | Password Policy (Min Length) | Medium | ⚠️ Review | Screenshot 6: Min=0 | Recommend enforcing minimum |
| 6 | Identity & Auth | Password History | Medium | ⚠️ Review | Screenshot 6: None | Recommend history tracking |
| 7 | Patch Management | Windows Version | Low | ✅ OK | Screenshot 1: Build 26200 | Current as of Sept 2026 |
| 8 | Patch Management | OS Updates | Low | ✅ OK | Screenshot 1: Current | Up to date |
| 9 | Patch Management | Hotfixes | Low | ✅ OK | Screenshot 2: 4 installed | Regularly patched |
| 10 | Patch Management | Security Software | Low | ✅ OK | Screenshot 7-9: Current | Signatures updated 12-09-2026 |
| 11 | Human Perimeter | Unnecessary Accounts | Low | ✅ OK | Screenshot 4: Only Sneha enabled | No shadow accounts |
| 12 | Human Perimeter | User Privilege Creep | Low | ✅ OK | Screenshot 5: 2 admins | Within normal range |
| 13 | Human Perimeter | Screen Lock Timeout | Low | ⚠️ Verify | Not shown in screenshots | Recommend <15 min |
| 14 | Network & Endpoint | Firewall Status | High | ✅ Fixed | Screenshot 12-13: All enabled | Enabled across 3 profiles |
| 15 | Network & Endpoint | Firewall Profiles | Low | ✅ OK | Screenshot 12-13: Domain/Private/Public | All configured |
| 16 | Network & Endpoint | Full-Disk Encryption | Critical | ⚠️ Pending | Not verified in screenshots | Requires BitLocker check |
| 17 | Network & Endpoint | Antivirus | Low | ✅ OK | Screenshot 7-9: Enabled | Real-time active |
| 18 | Network & Endpoint | Antispyware | Low | ✅ OK | Screenshot 7-9: Enabled | Signatures current |
| 19 | Network & Endpoint | NIS Protection | Low | ✅ OK | Screenshot 7-9: Enabled | Network intrusion detection |
| 20 | Network & Endpoint | Tamper Protection | Low | ✅ OK | Screenshot 7-9: Enabled | Anti-tampering active |

---

## Vulnerability Count by Severity

| Severity | Count | Details |
|----------|-------|---------|
| 🔴 Critical | 1 | Encryption status verification pending |
| 🟠 High | 0 | None identified |
| 🟡 Medium | 2 | Password policy review recommended |
| 🟢 Low | 0 | All low-risk items configured properly |
| ✅ Secure | 17 | Multiple security controls active |

---

## Key Strengths

✅ **Firewall:** All three profiles (Domain, Private, Public) are ENABLED  
✅ **Antivirus:** Windows Defender active with current signatures  
✅ **Account Management:** Disabled unnecessary built-in accounts  
✅ **Patch Status:** Current Windows version and hotfixes installed  
✅ **Security Features:** Secure Boot, UEFI protection, DMA protection enabled  
✅ **Real-time Protection:** Antivirus, antispyware, network inspection all active  

---

## Areas for Improvement

⚠️ **Password Policy:** Minimum length currently set to 0 (should be minimum 12)  
⚠️ **Password History:** Not tracking previous passwords (recommend 12-month history)  
⚠️ **Encryption:** BitLocker status requires explicit verification  
⚠️ **MFA:** Multi-factor authentication not confirmed in audit  

---

## Installed Software Review

### Office & Productivity
- Microsoft Office Home 2024
- OneDrive
- OneNote
- VLC Media Player (v3.0.23)

### Development Tools
- Python 3.14.4 (64-bit)
- Python development libraries

### Browsers
- Google Chrome (v152.0.7977.83)
- Microsoft Edge (v153.0.4234.32)
- Copilot (v153.0.4234.32)

### Security Assessment
✅ **Office:** Current  
✅ **Browsers:** Current (Chrome/Edge up to date)  
✅ **Python:** Recent version  
✅ **VLC:** No known critical CVEs  
✅ **Additional Tools:** Safe profile, no malicious software detected

---

## Next Steps (Post-Audit)

1. ☐ Verify BitLocker/Full-Disk Encryption status
2. ☐ Enforce minimum password length (12+ characters)
3. ☐ Enable password history tracking
4. ☐ Verify MFA setup on critical accounts (if applicable)
5. ☐ Set screen lock timeout to <15 minutes
6. ☐ Schedule quarterly security audits

---

**Audit Completed:** September 13, 2026  
**Next Review Date:** December 13, 2026 (Quarterly)
