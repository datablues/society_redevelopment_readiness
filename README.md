# Society Redevelopment Readiness (SRR_16_4_26)

Session started: 2026-04-16

## About
This repository stores all files, reports, and outputs generated during the Society Redevelopment Readiness project session.

## Session Summary
Exploring the feasibility of building a platform that aggregates Mumbai housing society redevelopment eligibility data from BMC, MHADA, SRA, RERA, and eCourts into a single standardized readiness report.

---

## Session 1 — Feasibility Analysis

**Date:** 2026-04-16

### Key Findings
- **Feasibility:** Medium — data exists but is fragmented; hybrid model recommended
- **Cost:** ~₹22–25L/year (lean) to ₹58–66L/year (scaled)
- **Competitors:** No funded startup has built this exact product; market dominated by offline PMC consultants
- **Gap:** No automated, self-serve, multi-source readiness report exists yet

### Files
- `Society_Redevelopment_Readiness_PDF.pdf` — Original document submitted for feasibility analysis

---

## Session 2 — Sample Report Generation (Evershine Nagar, Malad West)

**Date:** 2026-04-16

### Objective
Generate sample Society Redevelopment Readiness Reports for 4 buildings in Evershine Nagar, Malad West to validate the report format and scoring model.

### Buildings Covered

| Building | Year Built | Age | Score | Status |
|----------|-----------|-----|-------|--------|
| Manali Building CHS | 1983 | 43 yrs | 84/100 | HIGH READINESS |
| Nalanda Building CHS | 1990 | 36 yrs | 47/100 | MODERATE |
| Navjeevan Apartments CHS | 1986 | 40 yrs | 72/100 | READY |
| La Chapelle CHS | 2003 | 23 yrs | 18/100 | NOT YET ELIGIBLE |

### Readiness Scoring Framework
Reports are scored 0–100 based on:
- Building age (>30 years scores higher)
- Structural audit status
- Deemed Conveyance status
- Member consent (51% threshold under MCS Act)
- BMC C1/C2/C3 notices
- Litigation status (eCourts)
- Available FSI under DCPR 2034
- RERA redevelopment project registration

### Navjeevan Apartments — Verified Data
Real-world data was verified before generating the report:
- **BMC C1 Status:** CLEAR — not listed on BMC C1 Dangerous Buildings list (verified against Apr 2025 and 2022-23 lists at mcgm.gov.in)
- **RERA Status:** No active redevelopment project registered on maharera.maharashtra.gov.in
- **Occupancy:** Well Occupied — 40 units (1 BHK), original construction still in use
- **Developer on record:** KVC Developers (original construction only)
- **Readiness Score:** 72/100

### Data Sources Used
| Source | Purpose |
|--------|---------|
| mcgm.gov.in | BMC C1 Dangerous Buildings list (PDF) |
| maharera.maharashtra.gov.in | RERA project registration lookup |
| NoBroker, Square Yards | Occupancy and unit count verification |
| DCPR 2034 | FSI norms for redevelopment |
| MCS Act / Section 79A | PMC appointment and consent thresholds |

### Key Observations (Session 2)
- BMC portal uses iView — not programmatically accessible; C1 list is available as downloadable PDF (scrapeable)
- C2/C3 notices are not publicly listed — require manual ward office visits (validates hybrid model)
- No competitor has built an automated multi-source readiness report in this space

### Files Generated
- `generate_reports.py` — Python script using ReportLab to generate all reports
- `Manali_Building_CHS.pdf`
- `Nalanda_Building_CHS.pdf`
- `Navjeevan_Apartments_CHS.pdf`
- `La_Chapelle_CHS.pdf`

### GitHub Repository
https://github.com/datablues/society_redevelopment_readiness
