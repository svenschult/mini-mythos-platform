from flask import Flask, render_template, request
import os

from parser import parse_nmap_file
from analyzer import analyze_findings
from report import create_markdown_report

app = Flask(__name__)

SCAN_DIR = "scans"
REPORT_DIR = "reports"


@app.route("/")
def index():
    files = [f for f in os.listdir(SCAN_DIR) if f.endswith(".txt")]
    return render_template("index.html", files=files)


@app.route("/analyze", methods=["POST"])
def analyze():
    selected_file = request.form.get("scan_file")
    input_path = os.path.join(SCAN_DIR, selected_file)

    output_file = selected_file.replace(".txt", "_report.md")
    output_path = os.path.join(REPORT_DIR, output_file)

    findings = parse_nmap_file(input_path)
    analyzed = analyze_findings(findings)
    create_markdown_report(analyzed, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    return render_template("result.html", report=report_content)


if __name__ == "__main__":
    app.run(debug=True)