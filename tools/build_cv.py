# -*- coding: utf-8 -*-
"""cv.ops-center.org indirilebilir CV PDF ureteci.
Tek kolon, ATS-uyumlu. Madde imleri gercek Unicode bullet (U+2022) -- eski surumdeki
ZapfDingbats imleri metin cikariminda "q" olarak okunuyordu.
Icerik kaynagi: 1-GorkemKoc_CV_TR.pdf / 1-Gorkem_Koc_CV_EN.pdf
"""
from html import unescape

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, KeepTogether, HRFlowable, Table, TableStyle)

pdfmetrics.registerFont(TTFont("Calibri",  r"C:\Windows\Fonts\calibri.ttf"))
pdfmetrics.registerFont(TTFont("Calibri-B", r"C:\Windows\Fonts\calibrib.ttf"))
pdfmetrics.registerFontFamily("Calibri", normal="Calibri", bold="Calibri-B")

MARGIN_X  = 16*mm
CONTENT_W = A4[0] - 2*MARGIN_X

INK   = colors.HexColor("#14171c")
MUTED = colors.HexColor("#5a6270")
RULE  = colors.HexColor("#c9cfd8")

S = dict(
    name    = ParagraphStyle("name", fontName="Calibri-B", fontSize=23, leading=26, textColor=INK),
    title   = ParagraphStyle("title", fontName="Calibri-B", fontSize=11.5, leading=14,
                             textColor=colors.HexColor("#2f3742"), spaceBefore=2),
    contact = ParagraphStyle("contact", fontName="Calibri", fontSize=9, leading=12,
                             textColor=MUTED, spaceBefore=4),
    h       = ParagraphStyle("h", fontName="Calibri-B", fontSize=9.6, leading=12, textColor=INK,
                             spaceBefore=11, spaceAfter=3),
    body    = ParagraphStyle("body", fontName="Calibri", fontSize=9.6, leading=13, textColor=INK),
    role    = ParagraphStyle("role", fontName="Calibri-B", fontSize=10.6, leading=13, textColor=INK,
                             spaceBefore=7),
    meta    = ParagraphStyle("meta", fontName="Calibri", fontSize=8.8, leading=11.5, textColor=MUTED,
                             spaceBefore=1, spaceAfter=3),
    bullet  = ParagraphStyle("bullet", fontName="Calibri", fontSize=9.6, leading=12.8, textColor=INK,
                             leftIndent=9*mm, firstLineIndent=-4.6*mm, spaceAfter=2.2),
    tags    = ParagraphStyle("tags", fontName="Calibri", fontSize=8.5, leading=11, textColor=MUTED,
                             spaceBefore=2.5),
    skillLbl= ParagraphStyle("skillLbl", fontName="Calibri-B", fontSize=9.6, leading=12.8, textColor=INK),
    skillVal= ParagraphStyle("skillVal", fontName="Calibri", fontSize=9.6, leading=12.8, textColor=INK),
    line    = ParagraphStyle("line", fontName="Calibri", fontSize=9.6, leading=13, textColor=INK,
                             spaceAfter=1.5),
)

def _rule():
    return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=1, spaceAfter=4)

# Python'un str.upper() metodu 'i' -> 'I' verir; Turkce'de 'i' -> nokta li I (U+0130).
_TR_UP = str.maketrans({"i": "\u0130", "\u0131": "I"})

def _upper(text, lang):
    return (text.translate(_TR_UP) if lang == "tr" else text).upper()

def build(doc_data, out_path):
    lang = doc_data.get("lang", "en")
    story = []
    story.append(Paragraph(doc_data["name"], S["name"]))
    story.append(Paragraph(doc_data["title"], S["title"]))
    story.append(Paragraph(doc_data["contact"], S["contact"]))
    story.append(Spacer(1, 3))

    # Bolum basligi tek basina sayfa sonunda kalmasin: baslik + cizgi, kendisinden
    # sonraki ilk icerik parcasiyla birlikte KeepTogether'a sarilir.
    # KeepTogether ic ice gecirilmemeli (Reportlab tum grubu bir sonraki sayfaya atiyor);
    # bu yuzden "birlikte kalacaklar" tek duz liste olarak veriliyor.
    pending = []
    def emit(keep, rest=()):
        nonlocal pending
        group = pending + list(keep)
        story.append(KeepTogether(group) if len(group) > 1 else group[0])
        story.extend(rest)
        pending = []

    for kind, payload in doc_data["sections"]:
        if kind == "h":
            pending = [Paragraph(_upper(payload, lang), S["h"]), _rule()]
        elif kind == "p":
            emit([Paragraph(payload, S["body"])])
        elif kind == "job":
            head = [Paragraph(payload["role"], S["role"]), Paragraph(payload["meta"], S["meta"])]
            if payload["bullets"]:
                head.append(Paragraph("\u2022&nbsp;&nbsp;" + payload["bullets"][0], S["bullet"]))
            rest = [Paragraph("\u2022&nbsp;&nbsp;" + b, S["bullet"]) for b in payload["bullets"][1:]]
            if payload.get("tags"):
                rest.append(Paragraph(payload["tags"], S["tags"]))
            emit(head, rest)
        elif kind == "skills":
            # Her satir kendi tablosu: kolon genislikleri sabit oldugu icin etiketler
            # hizali kalir, ama blok tek parca olmadigindan sayfa sonunda takilmaz.
            lbl_w, gap = 40*mm, 3*mm
            widths = [lbl_w, CONTENT_W - lbl_w - gap]
            style = TableStyle([
                ("VALIGN",        (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING",   (0, 0), (0, -1), 0),
                ("LEFTPADDING",   (1, 0), (1, -1), gap),
                ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
                ("TOPPADDING",    (0, 0), (-1, -1), 1.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
            ])
            rows = []
            for l, t in payload:
                row = Table([[Paragraph(l, S["skillLbl"]), Paragraph(t, S["skillVal"])]],
                            colWidths=widths, hAlign="LEFT")
                row.setStyle(style)
                rows.append(row)
            emit(rows[:1], rows[1:])
        elif kind == "list":
            lines = [Paragraph(ln, S["line"]) for ln in payload]
            emit(lines[:1], lines[1:])

    def footer(canvas, docm):
        canvas.saveState()
        canvas.setFont("Calibri", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN_X, 11*mm, "cv.ops-center.org")
        canvas.drawRightString(A4[0]-MARGIN_X, 11*mm, f"{doc_data['page_word']} {docm.page}")
        canvas.restoreState()

    # Icerik metinleri Paragraph markup'i; PDF metadata duz metin ister.
    plain_title = unescape(doc_data["title"])
    pdf = BaseDocTemplate(out_path, pagesize=A4,
                          leftMargin=MARGIN_X, rightMargin=MARGIN_X,
                          topMargin=15*mm, bottomMargin=17*mm,
                          title=f"{doc_data['name']} — {plain_title}",
                          author=doc_data["name"], subject=plain_title,
                          creator="cv.ops-center.org")
    frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height, id="main",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    pdf.addPageTemplates([PageTemplate(id="pg", frames=[frame], onPage=footer)])
    pdf.build(story)
    return out_path
