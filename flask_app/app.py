import sys
import os

# Allow importing assignment1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request
from assignment1.scoring import calculate_match_score
from assignment1.evaluation import evaluate_match
import PyPDF2

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"txt", "pdf"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text(file):
    ext = file.filename.rsplit(".", 1)[1].lower()

    if ext == "txt":
        return file.read().decode("utf-8")

    if ext == "pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    return ""


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        resume_file = request.files.get("resume")
        jd_file = request.files.get("jd")

        if not resume_file or not jd_file:
            error = "Please upload both Resume and Job Description files."
        elif not allowed_file(resume_file.filename) or not allowed_file(jd_file.filename):
            error = "Only TXT or PDF files are allowed."
        else:
            resume_text = extract_text(resume_file)
            jd_text = extract_text(jd_file)

            if len(resume_text.strip()) < 50:
                error = "Resume content is too short."
            else:
                score, _, _, skills = calculate_match_score(resume_text, jd_text)
                match_type = evaluate_match(score)

                result = {
                    "score": score,
                    "match_type": match_type,
                    "skills": skills
                }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
