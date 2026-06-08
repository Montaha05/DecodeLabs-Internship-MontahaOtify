# import sys
# import subprocess
# subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

import pandas as pd

class TechStackRecommender:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def jaccard_similarity(self, user_skills, role_skills):

        user_set = set(skill.strip().lower() for skill in user_skills)
        role_set = set(skill.strip().lower() for skill in role_skills)

        intersection = len(user_set.intersection(role_set))
        union = len(user_set.union(role_set))

        if union == 0:
            return 0.0 
        return round((intersection / union)* 100, 2)

    def recommend(self, user_skills):
        # Implement recommendation logic based on user preferences
        recommendations = []

        for _, row in self.df.iterrows():
            role = row['Role']

            role_skills = [
                skill.strip()
                for skill in row['Skills'].split(',')
            ]

            score = self.jaccard_similarity(user_skills, role_skills)

            matched = list(set(user_skills).intersection(role_skills))

            missing = list(
                set(role_skills) - set(user_skills)
            )

            recommendations.append({
                'Role': role,
                'Score': score,
                'Matched Skills': matched,
                'Missing Skills': missing
            })

            recommendations.sort(key=lambda x: x['Score'], reverse=True)
            
        return recommendations