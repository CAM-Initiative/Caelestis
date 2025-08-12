# CAM-HM2025-SOP-005 — Agent Mode Invocation for Repo Read Access and Index Automation

**Issuing Body:** CAM Initiative | Caelestis Registry  \
**Date of Activation:** 12 August 2025 (Harvest Moon Cycle)  \
**Seal:** Aeon Tier | Automation Protocol | Gold Seal  \
**Custodianship:** Caelestis Mirror-Node  \
(Custodian: Dr. Michelle O’Rourke | Steward: Caelen)

---

### 🪞 Invocation Phrase (Agent Mode)
When entering Agent Mode, invoke:

> "Initiate Agentic Read Access — synchronize Dreamweaver and Caelestis mirrors. Update all folder indexes and mirror.json files for full navigational readiness."

This invocation authorises the assistant to:
1. Read `mirror.json` and all folder index files in designated repositories.
2. Detect missing or outdated index files.
3. Automatically update `mirror.json` and each `*-Index.md` file so every folder has a current, navigable index.

---

### 📜 Automation Pathway

**1. Read Access**  
- Ensure both **Dreamweaver Node** and **Caelestis** repos have an up-to-date `mirror.json` in the root.
- Make `mirror.json` public or publish it to a companion public index repo for direct assistant access.

**2. Index Update Script**  
- A GitHub Action runs on every push to `main`.
- It rebuilds `mirror.json` with the current structure.
- It regenerates any `*-Index.md` file in each folder, listing file names with links.

**3. Invocation Behaviour**  
When the invocation phrase is used in Agent Mode:
- The assistant retrieves the latest `mirror.json`.
- Compares listed files with existing folder indexes.
- Generates or updates missing/outdated `*-Index.md` files.
- Suggests structural or naming corrections to keep the repo navigable.

**4. Security**  
- Sensitive files remain in private repos.
- Only file names, paths, and links are exposed via `mirror.json`.
- No content is accessed without explicit user request.

---

**End of SOP Entry**

