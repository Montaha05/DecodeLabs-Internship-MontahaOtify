# AI Tech Stack Recommender

## Overview

AI-powered recommendation system that maps user skills to technology careers using similarity-based recommendation logic.

This project was developed as part of the DecodeLabs AI Internship Project 3: AI Recommendation Logic.

---

## Features

- Skill-based recommendations
- Similarity matching
- Career suggestions
- Skill gap analysis
- Learning roadmap generation

---

## Recommendation Logic

The system uses Jaccard Similarity.

Similarity Score =

Intersection(User Skills, Role Skills)
--------------------------------------
Union(User Skills, Role Skills)

The role with the highest similarity score is recommended first.

---

## Technologies

- Python
- Pandas
- Streamlit
- Recommendation Systems
- Similarity Matching

---

## Run Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Start application

```bash
streamlit run streamlit_app.py
```

---

## Example Input

```text
Python, SQL, Git
```

## Example Output

```text
1. Data Scientist - 40%
2. Backend Developer - 40%
3. Data Analyst - 33%
```

---

## Future Improvements

- TF-IDF similarity
- Cosine similarity
- User rating system
- Resume upload
- AI roadmap generator

---

## Author

Montaha Otify

Artificial Intelligence Intern at DecodeLabs