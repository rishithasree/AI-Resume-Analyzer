from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

RESULT_FILE = "results/all_resume_results.pdf"

def generate_pdf(name, status):

    if not os.path.exists("results"):
        os.makedirs("results")

    # If PDF already exists → read previous results
    records = []

    if os.path.exists(RESULT_FILE):
        with open("results/data.txt", "r") as f:
            records = f.readlines()

    # add new record
    records.append(f"{name} - {status}\n")

    # store records
    with open("results/data.txt", "w") as f:
        f.writelines(records)

    # generate PDF again with all records
    c = canvas.Canvas(RESULT_FILE, pagesize=letter)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 750, "AI Resume Analyzer Results")

    y = 700
    c.setFont("Helvetica", 14)

    for i, record in enumerate(records, start=1):
        name_status = record.strip().split(" - ")
        c.drawString(100, y, f"{i}. Name : {name_status[0]}")
        c.drawString(100, y-20, f"   Result : {name_status[1]}")
        y -= 60

    c.save()

    return RESULT_FILE