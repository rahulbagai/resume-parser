# Resume Parser

![Python Version](https://img.shields.io/pypi/pyversions/rb-resume-parser)
![PyPI Version](https://img.shields.io/pypi/v/rb-resume-parser)
![License](https://img.shields.io/pypi/l/rb-resume-parser)
![Downloads](https://img.shields.io/pypi/dm/rb-resume-parser)

![resume](https://img.shields.io/badge/-resume-blue) ![parser](https://img.shields.io/badge/-parser-blue) ![pdf](https://img.shields.io/badge/-pdf-blue) ![nlp](https://img.shields.io/badge/-nlp-blue) ![cv](https://img.shields.io/badge/-cv-blue)

Extract structured information from PDF resumes using NLP and pattern matching

## 📦 Installation

```bash
pip install rb-resume-parser
```


**Post-Install:**
```bash
Note: This package requires the spaCy English model.
Run: python -m spacy download en_core_web_sm
```

## 🚀 Quick Start

### Basic Usage

```python
from resume_parser import parse_resume

# Parse a resume PDF
result = parse_resume("sample_resume.pdf")

# Access extracted information
print(f"Name: {result['name']}")
print(f"Email: {result['email']}")
print(f"Phone: {result['phone']}")
print(f"LinkedIn: {result['linkedin']}")
print(f"Location: {result['location']}")
print(f"Role: {result['role']}")
print(f"Summary: {result['summary']}")

# Access achievements and awards
for achievement in result['achievements']:
    print(f"- {achievement['title']}")
    print(f"  {achievement['description']}")
    print(f"  Metric: {achievement['metric']}")

for award in result['awards']:
    print(f"- {award['title']}")
    print(f"  {award['description']}")
```

### Individual Extraction Functions

```python
from resume_parser import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_name,
    extract_location,
    extract_role,
    extract_summary,
    extract_achievements,
    extract_awards_and_honors
)
import spacy

# Load spaCy model (required for name and location extraction)
nlp = spacy.load("en_core_web_sm")

# Extract text from PDF
text = extract_text_from_pdf("sample_resume.pdf")

# Create NLP document for functions that need it
nlp_doc = nlp(text[:2000])  # Use first 2000 chars for efficiency

# Extract specific information
email = extract_email(text)
phone = extract_phone(text)
linkedin = extract_linkedin(text)
name = extract_name(text, nlp_doc)
location = extract_location(text, nlp_doc)
role = extract_role(text, name)
summary = extract_summary(text)
achievements = extract_achievements(text)
awards = extract_awards_and_honors(text)
```

### Processing Multiple Resumes

```python
from resume_parser import parse_resume
import os

resume_folder = "resumes/"
results = []

for filename in os.listdir(resume_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(resume_folder, filename)
        result = parse_resume(pdf_path)
        results.append(result)
        print(f"Processed: {filename}")

# Save results to JSON
import json
with open("parsed_resumes.json", "w") as f:
    json.dump(results, f, indent=2)
```

## 📚 Documentation

For full documentation, visit [https://github.com/rahulbagai/resume-parser](https://github.com/rahulbagai/resume-parser)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Maintained by [Rahul Bagai](https://github.com/rahulbagai/resume-parser)

## 📧 Contact

For questions and support, please open an issue on [GitHub](https://github.com/rahulbagai/resume-parser/issues).
