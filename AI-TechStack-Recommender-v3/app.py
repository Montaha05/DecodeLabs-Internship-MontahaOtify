from flask import Flask, render_template, request
from recommender import TechStackRecommender

app = Flask(__name__)

engine = TechStackRecommender('data/tech_roles.csv')
@app.route('/', methods=['GET', 'POST'])

def home():
    results = None

    if request.method == 'POST':
        skills = request.form['skills']
        user_skills = [s.strip() for s in skills.split(',')]
        results = engine.recommend(user_skills)


    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, port=5050)