# AI Tech Stack Recommender

A content-based recommendation system developed as part of DecodeLabs Artificial Intelligence Project 3.

## Overview

This project recommends technology career paths based on a user's skills.

The system compares user skills against predefined role requirements and calculates a similarity score for each role. Recommendations are then ranked from highest to lowest relevance.

## Features

* User skill input
* Content-based recommendation engine
* Similarity score calculation
* Recommended technology roles
* Matched skills display
* Missing skills analysis
* Flask web interface

## Recommendation Logic

For each role:

Similarity Score (%) =

(Number of Matching Skills / Total Skills Required for the Role) × 100

The roles are sorted by similarity score in descending order.

## Tech Stack

* Python
* Flask
* Pandas

## Project Structure

AI-TechStack-Recommender/

├── app.py

├── recommender.py

├── data/

│   └── tech_roles.csv

├── static/

│   └── script.js
│   └── style.css

├── templates/

│   └── index.html

├── README.md

├── requirements.txt

└── .gitignore

## Installation

Clone the repository:

git clone <repository-url>

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open:

http://127.0.0.1:5050

## Example

Input Skills:

Python, SQL, Machine Learning

Output:

* Machine Learning Engineer
* Data Scientist
* Data Analyst

with similarity scores and skill-gap analysis.

## Future Improvements

* Cosine Similarity
* TF-IDF Skill Weighting
* User Skill Rating
* Collaborative Filtering
* Recommendation Explanations
* Database Integration

## Author

Montaha Otify

Artificial Intelligence Intern at DecodeLabs
