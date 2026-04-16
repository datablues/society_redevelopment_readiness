from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import date
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Colour palette ──────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1B3A6B")
MID_BLUE    = colors.HexColor("#2E6DA4")
LIGHT_BLUE  = colors.HexColor("#D6E8F7")
GREEN       = colors.HexColor("#1E7E34")
LIGHT_GREEN = colors.HexColor("#D4EDDA")
AMBER       = colors.HexColor("#856404")
LIGHT_AMBER = colors.HexColor("#FFF3CD")
RED         = colors.HexColor("#721C24")
LIGHT_RED   = colors.HexColor("#F8D7DA")
GREY        = colors.HexColor("#6C757D")
LIGHT_GREY  = colors.HexColor("#F2F2F2")
WHITE       = colors.white

# ── Society data ─────────────────────────────────────────────────────────────
SOCIETIES = [
    {
        "name": "Manali Building CHS",
        "registration_no": "MUM/DBD/HSG/TC/9432/1984",
        "address": "Manali Building, Plot No. 14, Evershine Nagar,\nMalad (West), Mumbai – 400 064",
        "ward": "K-West (Malad)",
        "year_built": 1983,
        "age": 43,
        "floors": "Ground + 5",
        "total_flats": 30,
        "land_area_sqm": 620,
        "structure_type": "RCC Frame",
        "category": "Private CHS (Non-Cessed)",
        "structural_audit": "Completed – Category B (Minor Repairs Required)",
        "structural_audit_status": "DONE",
        "conveyance": "Deemed Conveyance Obtained (2019)",
        "conveyance_status": "DONE",
        "member_consent": "67% members have given written consent",
        "consent_pct": 67,
        "consent_status": "MET",
        "bmc_notice": "BMC Structural Audit Notice received (2023) – Complied",
        "bmc_status": "NOTICE COMPLIED",
        "mhada": "Not Listed",
        "sra": "Not Applicable",
        "fsi_available": "3.0 (DCPR 2034 – Suburban)",
        "rera_status": "Not Registered (pre-redevelopment stage)",
        "litigation": "None found (eCourts – Bombay HC & District Court)",
        "litigation_status": "CLEAR",
        "readiness_score": 84,
        "readiness_label": "HIGH READINESS",
        "readiness_color": "green",
        "recommended_next_steps": [
            "Appoint a Project Management Consultant (PMC) / Architect per Section 79A of MCS Act",
            "Commission a detailed structural report to upgrade from Category B to confirm redevelopment need",
            "Pass Special General Body Meeting (SGBM) resolution with 67% consent already secured",
            "Invite developer proposals / explore self-redevelopment option via MHADA scheme",
            "Register the redevelopment project under RERA once developer is finalised",
        ],
        "data_sources": [
            ("BMC Structural Audit Records", "K-West Ward Office, Malad"),
            ("Deemed Conveyance Certificate", "District Registrar, Borivali"),
            ("RERA Maharashtra Portal", "maharera.mahaonline.gov.in"),
            ("eCourts Case Search", "services.ecourts.gov.in"),
            ("DCPR 2034 FSI Norms", "mcgm.gov.in"),
        ],
        "summary": (
            "Manali Building CHS is well-positioned for redevelopment. At 43 years old, it exceeds the "
            "30-year threshold, has a valid deemed conveyance, a structural audit on record, and 67% member "
            "consent — above the mandatory 51%. No litigation is pending. The society's primary next action "
            "is to appoint a PMC and pass the SGBM resolution to formally initiate the process."
        ),
    },
    {
        "name": "Nalanda Building CHS",
        "registration_no": "MUM/DBD/HSG/TC/12876/1991",
        "address": "Nalanda Building, Plot No. 27-B, Evershine Nagar,\nMalad (West), Mumbai – 400 064",
        "ward": "K-West (Malad)",
        "year_built": 1990,
        "age": 36,
        "floors": "Ground + 7",
        "total_flats": 56,
        "land_area_sqm": 980,
        "structure_type": "RCC Frame",
        "category": "Private CHS (Non-Cessed)",
        "structural_audit": "Pending – Last audit expired in 2021, renewal overdue",
        "structural_audit_status": "PENDING",
        "conveyance": "Conveyance NOT obtained; Deemed Conveyance application filed (2024)",
        "conveyance_status": "IN PROGRESS",
        "member_consent": "38% members have given consent (below 51% threshold)",
        "consent_pct": 38,
        "consent_status": "NOT MET",
        "bmc_notice": "No BMC notice on record",
        "bmc_status": "CLEAR",
        "mhada": "Not Listed",
        "sra": "Not Applicable",
        "fsi_available": "2.7 (DCPR 2034 – Suburban)",
        "rera_status": "Not Registered",
        "litigation": "1 case pending – Member vs Society (Bombay HC, 2023)",
        "litigation_status": "CASE PENDING",
        "readiness_score": 47,
        "readiness_label": "MODERATE – ACTION NEEDED",
        "readiness_color": "amber",
        "recommended_next_steps": [
            "Renew structural audit immediately – engage a BMC-empanelled structural engineer",
            "Follow up on pending Deemed Conveyance application at District Registrar's office",
            "Conduct member awareness sessions to increase consent from 38% to 51%+",
            "Seek legal advice on the pending HC case before approaching developers",
            "Once litigation resolved and conveyance obtained, initiate SGBM for redevelopment resolution",
        ],
        "data_sources": [
            ("BMC Structural Audit Records", "K-West Ward Office, Malad"),
            ("Deemed Conveyance Application Status", "District Registrar, Borivali"),
            ("RERA Maharashtra Portal", "maharera.mahaonline.gov.in"),
            ("eCourts Case Search – HC Case No. 2023", "services.ecourts.gov.in"),
            ("DCPR 2034 FSI Norms", "mcgm.gov.in"),
        ],
        "summary": (
            "Nalanda Building CHS meets the age eligibility threshold at 36 years but has three key gaps "
            "that must be resolved before redevelopment can proceed: (1) the structural audit has lapsed and "
            "needs renewal, (2) deemed conveyance is in process but not yet secured, and (3) member consent "
            "at 38% is below the mandatory 51%. Additionally, a pending High Court case adds legal risk. "
            "The society should resolve these blockers before approaching developers."
        ),
    },
    {
        "name": "Navjeevan Apartments CHS",
        "registration_no": "MUM/DBD/HSG/TC/11204/1988",
        "address": "Navjeevan Apartments, Plot No. 22, Evershine Nagar,\nMalad (West), Mumbai – 400 064",
        "ward": "K-West (Malad)",
        "year_built": 1986,
        "age": 40,
        "floors": "Ground + 6",
        "total_flats": 42,
        "land_area_sqm": 750,
        "structure_type": "RCC Frame",
        "category": "Private CHS (Non-Cessed)",
        "structural_audit": "Completed – Category C (Structural Repairs Essential / Redevelopment Recommended)",
        "structural_audit_status": "DONE",
        "conveyance": "Deemed Conveyance Obtained (2021)",
        "conveyance_status": "DONE",
        "member_consent": "58% members have given written consent",
        "consent_pct": 58,
        "consent_status": "MET",
        "bmc_notice": "Not listed in BMC C1 Category (Dangerous Buildings) list — verified as on Apr 2025. No demolition/evacuation notice on public record.",
        "bmc_status": "CLEAR",
        "mhada": "Not Listed",
        "sra": "Not Applicable",
        "fsi_available": "3.0 (DCPR 2034 – Suburban)",
        "rera_status": "No RERA redevelopment project registration found. Building listed as 'Well Occupied' (40 units, 1 BHK) on property portals — original construction still in use. Developer on record: KVC Developers (original project).",
        "litigation": "None found (eCourts – Bombay HC & District Court)",
        "litigation_status": "CLEAR",
        "readiness_score": 72,
        "readiness_label": "HIGH READINESS",
        "readiness_color": "green",
        "recommended_next_steps": [
            "Appoint a PMC / Architect per Section 79A of MCS Act — Category C structural audit makes this urgent even without a BMC notice",
            "Convene Special General Body Meeting (SGBM) — 58% consent already exceeds the 51% mandatory threshold",
            "Obtain certified copy of Category C structural audit report and submit to BMC K-West Ward proactively",
            "Evaluate self-redevelopment option under MHADA scheme vs. developer-led redevelopment",
            "Register the redevelopment project under RERA once developer or self-redevelopment committee is finalised",
        ],
        "data_sources": [
            ("BMC C1 Dangerous Buildings List (Apr 2025)", "mcgm.gov.in — verified, not listed"),
            ("BMC C1 List 2022-23", "portal.mcgm.gov.in — verified, not listed"),
            ("Property Listing / Occupancy Status", "NoBroker, Square Yards — Well Occupied, 40 units"),
            ("RERA Maharashtra Portal", "maharera.maharashtra.gov.in — no redevelopment project found"),
            ("eCourts Case Search", "services.ecourts.gov.in — no cases found"),
            ("Deemed Conveyance Certificate", "District Registrar, Borivali"),
            ("DCPR 2034 FSI Norms", "mcgm.gov.in"),
        ],
        "summary": (
            "Navjeevan Apartments CHS is eligible and well-positioned for redevelopment. At 40 years old, it "
            "exceeds the 30-year threshold and has a Category C structural audit on record — the highest "
            "urgency rating. Deemed conveyance is obtained and 58% member consent exceeds the mandatory 51%. "
            "Verified data confirms: no BMC C1 demolition notice (Apr 2025 list checked), no active "
            "redevelopment project registered on RERA, and the building remains in original occupied condition "
            "(40 units). No litigation found. The society is ready to formally initiate redevelopment "
            "proceedings by appointing a PMC and passing the SGBM resolution."
        ),
    },
    {
        "name": "La Chapelle CHS",
        "registration_no": "MUM/DBD/HSG/TC/18543/2004",
        "address": "La Chapelle, Plot No. 8, Evershine Nagar,\nMalad (West), Mumbai – 400 064",
        "ward": "K-West (Malad)",
        "year_built": 2003,
        "age": 23,
        "floors": "Ground + 12",
        "total_flats": 96,
        "land_area_sqm": 1450,
        "structure_type": "RCC Frame (Post-2000 construction)",
        "category": "Private CHS (Non-Cessed)",
        "structural_audit": "Not Required – Building under 30 years",
        "structural_audit_status": "NOT APPLICABLE",
        "conveyance": "Conveyance Deed obtained from developer (2007)",
        "conveyance_status": "DONE",
        "member_consent": "Not assessed – building does not yet meet age eligibility",
        "consent_pct": 0,
        "consent_status": "NOT APPLICABLE",
        "bmc_notice": "No BMC notice on record",
        "bmc_status": "CLEAR",
        "mhada": "Not Listed",
        "sra": "Not Applicable",
        "fsi_available": "2.5 (DCPR 2034 – Suburban, post-2000 building)",
        "rera_status": "RERA Registered (original project) – Certificate No. P51800012341",
        "litigation": "None found (eCourts – Bombay HC & District Court)",
        "litigation_status": "CLEAR",
        "readiness_score": 18,
        "readiness_label": "NOT YET ELIGIBLE",
        "readiness_color": "red",
        "recommended_next_steps": [
            "No immediate redevelopment action required or recommended",
            "Ensure society maintenance fund is being built up for future repair needs",
            "Revisit redevelopment eligibility assessment in 2030 (building will be 27 years old)",
            "Keep track of any future policy changes under DCPR that may lower the age threshold",
            "Maintain building well to avoid premature structural degradation",
        ],
        "data_sources": [
            ("BMC Records", "K-West Ward Office, Malad"),
            ("Conveyance Deed", "District Registrar, Borivali"),
            ("RERA Maharashtra Portal", "maharera.mahaonline.gov.in"),
            ("eCourts Case Search", "services.ecourts.gov.in"),
            ("DCPR 2034 FSI Norms", "mcgm.gov.in"),
        ],
        "summary": (
            "La Chapelle CHS, at 23 years old, does not yet meet the minimum 30-year age criterion for "
            "redevelopment eligibility under DCPR 2034 and the Maharashtra Co-operative Societies Act. "
            "The building is structurally sound, has a valid conveyance deed, and is free of litigation. "
            "No redevelopment action is advised at this stage. The society should reassess readiness around 2030."
        ),
    },
]

# ── Styles ────────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["cover_title"] = ParagraphStyle(
        "cover_title", fontSize=22, textColor=WHITE,
        fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=6
    )
    styles["cover_sub"] = ParagraphStyle(
        "cover_sub", fontSize=13, textColor=LIGHT_BLUE,
        fontName="Helvetica", alignment=TA_CENTER, spaceAfter=4
    )
    styles["cover_meta"] = ParagraphStyle(
        "cover_meta", fontSize=10, textColor=colors.HexColor("#BBCFE8"),
        fontName="Helvetica", alignment=TA_CENTER, spaceAfter=2
    )
    styles["section_header"] = ParagraphStyle(
        "section_header", fontSize=11, textColor=WHITE,
        fontName="Helvetica-Bold", alignment=TA_LEFT, spaceAfter=0,
        leftIndent=6
    )
    styles["body"] = ParagraphStyle(
        "body", fontSize=9.5, textColor=colors.black,
        fontName="Helvetica", spaceAfter=4, leading=14
    )
    styles["label"] = ParagraphStyle(
        "label", fontSize=9, textColor=GREY,
        fontName="Helvetica-Bold", spaceAfter=2
    )
    styles["value"] = ParagraphStyle(
        "value", fontSize=9.5, textColor=colors.black,
        fontName="Helvetica", spaceAfter=2
    )
    styles["disclaimer"] = ParagraphStyle(
        "disclaimer", fontSize=7.5, textColor=GREY,
        fontName="Helvetica-Oblique", alignment=TA_CENTER, leading=10
    )
    styles["footer"] = ParagraphStyle(
        "footer", fontSize=8, textColor=GREY,
        fontName="Helvetica", alignment=TA_CENTER
    )
    styles["score_big"] = ParagraphStyle(
        "score_big", fontSize=36, fontName="Helvetica-Bold",
        alignment=TA_CENTER, spaceAfter=0
    )
    styles["score_label"] = ParagraphStyle(
        "score_label", fontSize=11, fontName="Helvetica-Bold",
        alignment=TA_CENTER, spaceAfter=0
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", fontSize=9.5, textColor=colors.black,
        fontName="Helvetica", spaceAfter=3, leftIndent=12,
        bulletIndent=0, leading=13
    )
    return styles


# ── Helpers ───────────────────────────────────────────────────────────────────
def section_title(text, styles):
    header = Table(
        [[Paragraph(text, styles["section_header"])]],
        colWidths=["100%"]
    )
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
    ]))
    return header


def kv_table(rows, styles, col_widths=None):
    """Two-column key-value table."""
    if col_widths is None:
        col_widths = [55 * mm, 110 * mm]
    data = []
    for k, v in rows:
        data.append([
            Paragraph(k, styles["label"]),
            Paragraph(v, styles["value"]),
        ])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), LIGHT_GREY),
        ("BACKGROUND", (1, 0), (1, -1), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def status_badge(text, status):
    """Coloured status badge."""
    colors_map = {
        "green":  (GREEN,       LIGHT_GREEN),
        "amber":  (AMBER,       LIGHT_AMBER),
        "red":    (RED,         LIGHT_RED),
        "grey":   (GREY,        LIGHT_GREY),
        "blue":   (MID_BLUE,    LIGHT_BLUE),
    }
    fg, bg = colors_map.get(status, (GREY, LIGHT_GREY))
    style = ParagraphStyle(
        "badge", fontSize=8.5, fontName="Helvetica-Bold",
        textColor=fg, alignment=TA_CENTER
    )
    t = Table([[Paragraph(text, style)]], colWidths=[45 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.6, fg),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return t


def checklist_table(items, styles):
    """Eligibility checklist with coloured status column."""
    status_color = {
        "DONE": "green", "MET": "green", "CLEAR": "green",
        "NOTICE COMPLIED": "green",
        "PENDING": "amber", "IN PROGRESS": "amber",
        "NOT MET": "red", "CASE PENDING": "red",
        "NOT APPLICABLE": "grey", "N/A": "grey",
    }
    data = [
        [
            Paragraph("<b>Check</b>", styles["label"]),
            Paragraph("<b>Finding</b>", styles["label"]),
            Paragraph("<b>Status</b>", styles["label"]),
        ]
    ]
    for check, finding, status in items:
        col = status_color.get(status, "grey")
        data.append([
            Paragraph(check, styles["value"]),
            Paragraph(finding, styles["value"]),
            status_badge(status, col),
        ])

    t = Table(data, colWidths=[45 * mm, 100 * mm, 20 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT_BLUE),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_GREY]),
    ]))
    return t


def score_panel(score, label, color, styles):
    text_color = {"green": GREEN, "amber": AMBER, "red": RED}[color]
    bg_color   = {"green": LIGHT_GREEN, "amber": LIGHT_AMBER, "red": LIGHT_RED}[color]

    score_style = ParagraphStyle(
        "sp", fontSize=40, fontName="Helvetica-Bold",
        textColor=text_color, alignment=TA_CENTER
    )
    label_style = ParagraphStyle(
        "sl", fontSize=10, fontName="Helvetica-Bold",
        textColor=text_color, alignment=TA_CENTER
    )
    sub_style = ParagraphStyle(
        "ss", fontSize=8, fontName="Helvetica",
        textColor=GREY, alignment=TA_CENTER
    )

    inner = Table([
        [Paragraph(f"{score}", score_style)],
        [Paragraph(label, label_style)],
        [Paragraph("out of 100", sub_style)],
    ], colWidths=[60 * mm])
    inner.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    outer = Table([[inner]], colWidths=[60 * mm])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_color),
        ("BOX", (0, 0), (-1, -1), 1.2, text_color),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return outer


# ── Main report builder ───────────────────────────────────────────────────────
def build_report(society):
    filename = os.path.join(
        OUTPUT_DIR,
        society["name"].replace(" ", "_").replace("/", "-") + ".pdf"
    )
    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=18 * mm, bottomMargin=18 * mm
    )
    styles = build_styles()
    story  = []
    W      = 174 * mm   # usable width

    # ── Cover / Header ─────────────────────────────────────────────────────
    cover_data = [
        [Paragraph("SOCIETY REDEVELOPMENT READINESS REPORT", styles["cover_title"])],
        [Paragraph(society["name"], ParagraphStyle(
            "cn", fontSize=16, textColor=WHITE,
            fontName="Helvetica-Bold", alignment=TA_CENTER
        ))],
        [Paragraph(society["address"].replace("\n", "<br/>"),
                   styles["cover_sub"])],
        [Spacer(1, 4)],
        [Paragraph(
            f"Ward: {society['ward']}  |  Report Date: {date.today().strftime('%d %B %Y')}  |  "
            f"Prepared by: SRR Platform (Sample Report)",
            styles["cover_meta"]
        )],
    ]
    cover = Table(cover_data, colWidths=[W])
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    story.append(cover)
    story.append(Spacer(1, 8))

    # ── Readiness Score + Summary side by side ─────────────────────────────
    summary_style = ParagraphStyle(
        "sum", fontSize=9.5, textColor=colors.black,
        fontName="Helvetica", leading=14, spaceAfter=0
    )
    score_cell  = score_panel(
        society["readiness_score"],
        society["readiness_label"],
        society["readiness_color"],
        styles
    )
    summary_cell = Table(
        [[Paragraph("<b>Executive Summary</b>", styles["label"])],
         [Paragraph(society["summary"], summary_style)]],
        colWidths=[108 * mm]
    )
    summary_cell.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    top_row = Table(
        [[score_cell, summary_cell]],
        colWidths=[65 * mm, 109 * mm]
    )
    top_row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(top_row)
    story.append(Spacer(1, 10))

    # ── Section 1: Society Profile ─────────────────────────────────────────
    story.append(section_title("1. Society Profile", styles))
    story.append(Spacer(1, 4))
    profile_rows = [
        ("Registration No.",   society["registration_no"]),
        ("Address",            society["address"].replace("\n", "<br/>")),
        ("BMC Ward",           society["ward"]),
        ("Year of Construction", str(society["year_built"])),
        ("Age of Building",    f"{society['age']} years"),
        ("Structure",          f"{society['floors']} floors  |  {society['total_flats']} flats  |  {society['land_area_sqm']} sq.m. land"),
        ("Construction Type",  society["structure_type"]),
        ("Society Category",   society["category"]),
    ]
    story.append(kv_table(profile_rows, styles))
    story.append(Spacer(1, 10))

    # ── Section 2: Eligibility Checklist ───────────────────────────────────
    story.append(section_title("2. Redevelopment Eligibility Checklist", styles))
    story.append(Spacer(1, 4))

    checklist_items = [
        ("Building Age (≥30 yrs)",
         f"Built {society['year_built']} — {society['age']} years old",
         "DONE" if society["age"] >= 30 else "NOT MET"),
        ("Structural Audit",
         society["structural_audit"],
         society["structural_audit_status"]),
        ("Conveyance / Deemed Conveyance",
         society["conveyance"],
         society["conveyance_status"]),
        ("Member Consent (≥51%)",
         society["member_consent"],
         society["consent_status"]),
        ("BMC Notice Status",
         society["bmc_notice"],
         society["bmc_status"]),
        ("MHADA Classification",
         society["mhada"],
         "N/A"),
        ("SRA Eligibility",
         society["sra"],
         "N/A"),
        ("FSI Available (DCPR 2034)",
         society["fsi_available"],
         "DONE"),
        ("RERA Registration",
         society["rera_status"],
         "N/A"),
        ("Litigation / Court Cases",
         society["litigation"],
         society["litigation_status"]),
    ]
    story.append(KeepTogether(checklist_table(checklist_items, styles)))
    story.append(Spacer(1, 10))

    # ── Section 3: Recommended Next Steps ─────────────────────────────────
    story.append(section_title("3. Recommended Next Steps", styles))
    story.append(Spacer(1, 4))
    for i, step in enumerate(society["recommended_next_steps"], 1):
        story.append(Paragraph(f"<b>{i}.</b> {step}", styles["bullet"]))
    story.append(Spacer(1, 10))

    # ── Section 4: Data Sources ────────────────────────────────────────────
    story.append(section_title("4. Data Sources", styles))
    story.append(Spacer(1, 4))
    src_data = [[
        Paragraph("<b>Source</b>", styles["label"]),
        Paragraph("<b>Authority / Portal</b>", styles["label"]),
    ]]
    for src, authority in society["data_sources"]:
        src_data.append([
            Paragraph(src, styles["value"]),
            Paragraph(authority, styles["value"]),
        ])
    src_table = Table(src_data, colWidths=[95 * mm, 79 * mm])
    src_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT_BLUE),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_GREY]),
    ]))
    story.append(src_table)
    story.append(Spacer(1, 12))

    # ── Disclaimer ─────────────────────────────────────────────────────────
    story.append(HRFlowable(width=W, thickness=0.5, color=GREY))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "DISCLAIMER: This is a SAMPLE report generated for feasibility demonstration purposes only. "
        "All data is illustrative and does not represent verified or legally binding information. "
        "Before making any redevelopment decision, societies must engage a licensed structural engineer, "
        "legal counsel, and a registered PMC. Verify all data independently from official government portals.",
        styles["disclaimer"]
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f"SRR Platform — Society Redevelopment Readiness Report  |  Evershine Nagar, Malad West, Mumbai  |  {date.today().strftime('%d %B %Y')}",
        styles["footer"]
    ))

    doc.build(story)
    print(f"  Generated: {os.path.basename(filename)}")
    return filename


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    target = sys.argv[1].lower() if len(sys.argv) > 1 else None
    to_generate = [s for s in SOCIETIES if target is None or target in s["name"].lower()]
    print("Generating Society Redevelopment Readiness Reports...")
    print(f"Output folder: {OUTPUT_DIR}\n")
    for society in to_generate:
        build_report(society)
    print(f"\nDone. {len(to_generate)} report(s) generated.")
