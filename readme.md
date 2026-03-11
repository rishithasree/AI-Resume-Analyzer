# AI Resume Analyzer

AI Resume Analyzer is a web application built using Python and Flask that analyzes resumes in PDF format. The system extracts text from uploaded resumes, detects important technical skills, calculates a resume score, and determines whether the candidate is qualified or not qualified.

The application also generates a centralized PDF report that stores the results of all analyzed resumes in one file.

---

## Features

- Upload resumes in PDF format
- Extract text from resumes automatically
- Detect technical skills such as Python, Java, HTML, CSS, SQL, etc.
- Generate a resume score based on detected skills
- Show whether the candidate is Qualified or Not Qualified
- Store results of multiple candidates in a single PDF report
- Simple and interactive user interface
- Built using Flask and Python

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- PyPDF2 (for extracting text from resumes)
- ReportLab (for generating PDF reports)

---

## Project Structure
AI-Resume-Analyzer
│
├── app.py
├── resume_analyzer.py
├── pdf_generator.py
├── requirements.txt
│
├── uploads
│
├── results
│ └── all_resume_results.pdf
│
├── static
│ ├── css
│ │ └── style.css
│ ├── js
│ │ └── script.js
│ └── images
│ └── logo.png
│
└── templates
├── layout.html
├── index.html
└── result.html


Install the required dependencies:
pip install -r requirements.txt


---

## Running the Application

Run the Flask application:
python app.py


Open your browser and go to:

http://127.0.0.1:5000


---

## How It Works

1. The user uploads a resume in PDF format.
2. The system extracts text from the PDF.
3. It searches for predefined technical skills in the resume.
4. A resume score is calculated based on detected skills.
5. If the score is greater than or equal to the threshold, the candidate is marked as **Qualified**, otherwise **Not Qualified**.
6. The result is displayed on the webpage.
7. The candidate name and result are stored in a centralized PDF report.

---

## Example Output

Resume Score: 70 / 100

Skills Found:
- Python
- Machine Learning
- SQL

Result: Qualified

---

## Future Improvements

- AI-based skill extraction using NLP
- Job role recommendation
- Resume improvement suggestions
- Resume ranking system
- Dashboard for recruiters

---

## Author

Rishitha Tarra

---

## License

This project is for educational and learning purposes.