from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF

app = Flask(__name__)
CORS(app)

# ✅ Embedded skills list
SKILLS_DB = [
    "python", "javascript", "react", "node.js", "django", "flask", "sql",
    "html", "css", "machine learning", "data analysis", "pandas", "numpy",
    "excel", "project management", "communication", "git", "linux", "docker",
    "aws", "azure", "tensorflow", "keras", "nlp", "deep learning", "api"
]

def extract_text(file):
    if file.filename.endswith(".pdf"):
        # Extract text using PyMuPDF
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join([page.get_text() for page in doc])
    elif file.filename.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

def extract_skills(text):
    text = text.lower()
    return sorted(set([skill for skill in SKILLS_DB if skill in text]))

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    text = extract_text(file)
    skills = extract_skills(text)
    return jsonify({"skills": skills})

if __name__ == "__main__":
    app.run(debug=True)
