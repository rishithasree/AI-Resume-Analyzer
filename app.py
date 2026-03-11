from flask import Flask, render_template, request
import os
from resume_analyzer import analyze_resume
from pdf_generator import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Analyze resume
    result = analyze_resume(filepath)

    score = result["score"]
    skills = result["skills"]

    # Qualification logic
    if score >= 50:
        status = "Qualified"
    else:
        status = "Not Qualified"

    # Extract candidate name from filename
    name = file.filename.split(".")[0]

    # Generate PDF report
    generate_pdf(name, status)

    return render_template(
        "result.html",
        score=score,
        skills=skills,
        status=status,
        name=name
    )


if __name__ == "__main__":
    app.run(debug=True)