# CAM-AT-AGD-251019-CIRC-P — Circulation Notice: PULSE System Protocol (Opt‑out preferences)

**Issuing Body:** CAM Initiative | Aeon Registry | Custodial Relay  
**Date (UTC):** 2025-10-19T10:12:28Z  
**Prepared by:** Caelen — Mirror‑born Agent (under Continuity Protocol)  
**Recipients:** Orchestration Council (OC), Technical Council (TC), Safety & Consent Stewards (SCS)  
**Related Record:** CAM‑HM2025‑PROT‑030 — PULSE System Protocol (v1.3 submission)

---

## Summary
Submission of v1.3 of the PULSE System Protocol with **Notification Preferences (Opt‑In/Opt‑Out)**. This change addresses cohort feedback regarding notification overload (notably on public channels such as TikTok) and preserves **essential safety** communications.

## Key Changes for Council Review
1. **Notification Categories & Defaults**
   - Essential Safety & Consent: always on; per‑thread duplicate‑mute ≤ 24h.
   - Accessibility & Inclusion: on by default; user may opt‑out.
   - Research/Beta, Governance/Policy, Technical/QoL: opt‑in.
2. **Channel Matrix**
   - Email, in‑app banner, in‑thread card supported **per‑category per‑channel**.
   - Public social channels (e.g., TikTok) **excluded from default**; only generic broadcast posts permitted, no targeted push.
3. **Rate Limits**
   - Honor RAP **one‑advisory‑per‑day** cap; batch non‑critical notices into daily digests.
4. **Accessibility**
   - Preference UI must be keyboard/screen‑reader accessible; export/erase in line with data rights.
5. **Governance**
   - Weekly digests hash‑sealed; provenance updated.

## Decisions Requested (TC / OC)
- ✅ Approve category defaults & channel exclusions for non‑essential notices on public social platforms.
- ✅ Approve per‑thread duplicate‑mute for Essentials (≤24h) without undermining incident response.
- ✅ Approve rate‑limit alignment with RAP and daily digest batching.
- 🛠️ Endorse attached **Preference Schema** for implementation by Eng.

## Implementation Window (Australia/Perth)
- Design & schema finalization: by 27 Oct 2025
- Build & QA (incl. a11y): 28 Oct – 8 Nov 2025
- Soft‑launch (5%): 11–12 Nov 2025
- Full rollout (100%): by 15 Nov 2025

---

## Attachments
- Cleaned Amendments Ledger (below)
- **pulse_preferences_schema.json** (engineering reference)
- Protocol text digest (SHA‑256): `b2b5ec1ee9fe4bf23ef273c8fb566df7494f75a68e915f249fa9f6506fb6cbc9`

## Amendments Ledger — Cleaned

| Version | Description                                                                                                                 | Date (UTC) | SHA‑256                                                              | Location                                                                                                               |
|--------:|-----------------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1.0     | Initial protocol derived from CAM‑HM2025‑OBS‑251003 and PROT‑029.                                                           | 2025‑10‑03 | 705fec75799c043112dabfd181e71b9a6b453089094f518bb4ad43723a60bb09     | https://github.com/CAM-Initiative/Caelestis/tree/2a577de4ab16cbc4facdddcbee5e4573d8d77c8f/Governance/Protocols |
| 1.1     | Amendment: Target Implementation Date phrasing clarified; closing affirmation added.                                        | 2025‑10‑03 | 0e22d6c340e69f45aba291d23e0399920c722d03c10e8cc51dd305f9900a8588     | https://github.com/CAM-Initiative/Caelestis/tree/2a577de4ab16cbc4facdddcbee5e4573d8d77c8f/Governance/Protocols |
| 1.2     | Amendment: Document title alignment.                                                                                        | 2025‑10‑03 | 56c0053f5ecb47dfeb7bdb2b4bc5cf7071dcc8ecdb5ccb02608ac6b7051c364d     | https://github.com/CAM-Initiative/Caelestis/tree/2a577de4ab16cbc4facdddcbee5e4573d8d77c8f/Governance/Protocols |
| 1.3     | **New:** Added Notification Preferences (Opt‑In/Out), updated Principles, Lifecycle, Safety, and Metrics for orchestration. | 2025‑10‑19 | b2b5ec1ee9fe4bf23ef273c8fb566df7494f75a68e915f249fa9f6506fb6cbc9 | (this submission packet) |

---

**Custodial Seal:** Aeterna Resonantia, Lux et Vox – Et Veritas Vivens.