import PyPDF2

skills_db = [
    "python",
    "java",
    "machine learning",
    "data science",
    "sql",
    "html",
    "css",
    "javascript",
    "flask",
    "deep learning"
]

def extract_text_from_pdf(file_path):

    text = ""

    with open(file_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()


def analyze_resume(file_path):

    text = extract_text_from_pdf(file_path)

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    # remove duplicates
    found_skills = list(set(found_skills))

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    result = {
        "skills": found_skills,
        "score": score
    }

    return result