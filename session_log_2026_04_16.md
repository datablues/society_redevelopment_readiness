# Session Log — 2026-04-16

## Project: Society Redevelopment Readiness (SRR_16_4_26)

---

## What Was Done

### 1. Project Setup
- Created local folder: `C:\Users\chira\Downloads\SRR_16_4_26\`
- Linked to GitHub repo: https://github.com/datablues/society_redevelopment_readiness.git
- Renamed branch from `master` to `main` (force push used to resolve GitHub placeholder commit conflict)

### 2. Sample Reports — Evershine Nagar, Malad West
Generated Society Redevelopment Readiness Reports (PDFs) for 4 buildings using `generate_reports.py` (ReportLab):

| Building | Score | Status |
|----------|-------|--------|
| Manali Building CHS | 84/100 | HIGH READINESS |
| Nalanda Building CHS | 47/100 | MODERATE |
| Navjeevan Apartments CHS | 72/100 | READY |
| La Chapelle CHS | 18/100 | NOT YET ELIGIBLE |

### 3. Navjeevan Apartments — Real Data Verification
Verified against public sources before generating report:

**BMC C1 Status:**
- Checked BMC C1 Dangerous Buildings list (2022-23 PDF and Apr 2025 PDF from mcgm.gov.in)
- Navjeevan Apartments NOT listed on either list
- BMC status set to CLEAR

**RERA Status:**
- Searched maharera.maharashtra.gov.in for redevelopment project
- No active redevelopment project found
- Building listed as "Well Occupied" (40 units, 1 BHK) on property portals
- Developer on record: KVC Developers (original construction only)

**Readiness Score:** Adjusted to 72/100 based on verified data

### 4. GitHub Push
All files committed and pushed to `main`:
- `generate_reports.py`
- `Manali_Building_CHS.pdf`
- `Nalanda_Building_CHS.pdf`
- `Navjeevan_Apartments_CHS.pdf`
- `La_Chapelle_CHS.pdf`
- `README.md`

Commit: `fca34e6` — "Add Society Redevelopment Readiness reports for Evershine Nagar, Malad West"

---

## Technical Notes

### Report Generation
- Library: `reportlab` (pip install reportlab)
- Script: `generate_reports.py`
- Run all reports: `python generate_reports.py`
- Run single report: `python generate_reports.py navjeevan`

### BMC Portal Findings
- Main portal (mcgm.gov.in) uses iView — not accessible via automated scraping
- C1 buildings list is published as a downloadable PDF — can be scraped/parsed
- C2/C3 notices are NOT publicly listed — require manual ward office visits
  - This validates the hybrid model (automated + manual verification)

### Data Sources
| Source | URL | Notes |
|--------|-----|-------|
| BMC C1 List | mcgm.gov.in/assets/pdf/... | PDF download, parseable |
| RERA Maharashtra | maharera.maharashtra.gov.in | Project search by location |
| eCourts | ecourts.gov.in | Litigation search |
| NoBroker / Square Yards | Property portals | Occupancy verification |
| DCPR 2034 | — | FSI norms for Mumbai |

---

## Next Steps (Suggested)
1. Run reports for more societies/areas to stress-test the scoring model
2. Build a web scraper for the BMC C1 PDF list (published quarterly)
3. Explore RERA API or structured data export
4. Design the product workflow: data ingestion → scoring → report generation → delivery

---

## Files in This Session
```
SRR_16_4_26/
├── README.md
├── session_log_2026_04_16.md          ← this file
├── generate_reports.py
├── Society_Redevelopment_Readiness_PDF.pdf
├── Manali_Building_CHS.pdf
├── Nalanda_Building_CHS.pdf
├── Navjeevan_Apartments_CHS.pdf
└── La_Chapelle_CHS.pdf
```
