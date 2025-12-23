from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import red, darkgreen
import os

app = Flask(__name__)

FONT_PATH = "fonts/UnifrakturCook-Bold.ttf"
pdfmetrics.registerFont(TTFont("Gothic", FONT_PATH))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]

    file_path = f"/tmp/{name}_Christmas_Gift.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)

    style = ParagraphStyle(
        name="GothicStyle",
        fontName="Gothic",
        fontSize=32,
        alignment=1,
        textColor=darkgreen
    )

    content = []
    content.append(Spacer(1, 80))
    content.append(Paragraph("🎄 Merry Christmas 🎄", style))
    content.append(Spacer(1, 40))

    content.append(
        Paragraph(f"Dear <font color='red'>{name}</font>,<br/>"
                  "May your days be filled with joy, peace, and wonder.",
                  style)
    )

    content.append(Spacer(1, 40))
    content.append(Paragraph("— Santa Claus 🎅", style))

    doc.build(content)

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
