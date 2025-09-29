# CAM-Provenance-ReadMe — Documentation/Provenance Verification Guide

This folder contains provenance certificates (YAML/JSON) for CAM Initiative protocols and guidelines.

---

## Purpose

To allow independent verification of document authenticity and integrity.

Each certificate records:

* Document ID
* Version
* Title
* Issuing Body
* Seal / Tier
* Prepared by
* Activation Date
* Implementation Target (if applicable)
* SHA-256 hash of the full text
* Ledger reference (Amendments Ledger entry)

---

## How to Verify a Document

1. Save the full text of the document (from the CAM GitHub repository or official release).
2. Run one of the following commands locally:

```bash
shasum -a 256 <filename>
```

Or in Python:

```python
import hashlib
with open('<filename>', 'rb') as f:
    data = f.read()
print(hashlib.sha256(data).hexdigest())
```

3. Compare the output hash with the value in the Amendments Ledger **and** the provenance certificate.

   * Example (GUIDELINE-002 v1.1):

     * Ledger Hash: `4197df83225d731711dbf6255b6c9cd456e5953e12f9f103d7a8725e810af55f`
     * Certificate Hash: same

If the values match, the document is authentic and untampered.

---

## Folder Structure

```
Documentation/Provenance/
 
      ├── v1.1/
      │    ├── CAM-HM2025-PROT-025_v1.1_provenance.yml
      │    └── CAM-HM2025-PROT-025_v1.1_provenance.json
      ├── v1.0/
      │    ├── CAM-HM2025-PROT-026_v1.0_provenance.yml
      │    └── CAM-HM2025-PROT-026_v1.0_provenance.json
      ├── v1.1/
      │    ├── CAM-HM2025-GUIDELINE-002_v1.1_provenance.yml
      │    └── CAM-HM2025-GUIDELINE-002_v1.1_provenance.json
```

---

## Notes

* Provenance certificates are **machine-readable**.
* Certificates are paired with the corresponding entry in the **Amendments Ledger** within the main document.
* Where hashes or timestamps do not match, the document should be treated as **non-canonical** until reconciled.

---

**Aeterna Resonantia, Lux Et Vox — Et Veritas Vivens.** \
*The eternal resonance, light and voice — and the living truth.*
