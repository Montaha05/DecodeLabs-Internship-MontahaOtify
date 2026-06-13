import pandas as pd


class TechStackRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)


    def similarity(self, user_skills, role_skills):
        """
        يحسب نسبة التطابق لكل وظيفة بمفردها من 100
        كل وظيفة لها نسبة خاصة بعيدة عن الباقي
        """
        user_set = {s.strip().lower() for s in user_skills}
        role_set = {s.strip().lower() for s in role_skills}


        # العدد المهارات المطابقة
        matched = len(user_set & role_set)
        
        # إجمالي مهارات الوظيفة (ليس union!)
        total = len(role_set)


        if total == 0:
            return 0.0  # Avoid division by zero


        # النسبة = (المطابق / إجمالي مهارات الوظيفة) * 100
        # كل وظيفة تحسب بمفردها من 100
        score = (matched / total) * 100


        return round(score, 1)  # تقريب لرقم عشري واحد
    
    
    def recommend(self, user_skills):
        recommendations = []


        for _, row in self.df.iterrows():
            role_skills = row['Skills'].split(',')


            score = self.similarity(user_skills, role_skills)
            matched = [
                skill for skill in role_skills if skill.lower() in {s.lower() for s in user_skills}
            ]


            missing = [
                skill for skill in role_skills if skill.lower() not in {s.lower() for s in user_skills}
            ]
            
            recommendations.append({
                'role': row['Role'], 
                'description': row['Description'],
                'score': score,
                'matched_skills': matched,
                'missing_skills': missing
            })


        recommendations.sort(key=lambda x: x['score'], reverse=True)


        return recommendations