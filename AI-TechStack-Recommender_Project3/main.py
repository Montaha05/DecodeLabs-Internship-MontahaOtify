from recommender import TechStackRecommender


def main():

    print("=" * 50)
    print("AI TECH STACK RECOMMENDER")
    print("=" * 50)

    skills = input(
        "\nEnter your skills (comma separated): "
    )

    user_skills = [
        skill.strip()
        for skill in skills.split(",")
    ]

    recommender = TechStackRecommender(
        "data/raw_skills.csv"
    )

    recommendations = recommender.recommend(
        user_skills
    )

    print("\nTOP 5 RECOMMENDATIONS")
    print("=" * 50)

    for i, rec in enumerate(
            recommendations[:5], start=1):

        print(f"\n{i}. {rec['Role']}")
        print(f"Match Score: {rec['Score']}%")

        print(
            "Matched Skills:",
            ", ".join(rec["Matched Skills"])
            if rec["Matched Skills"] else "None"
        )

        print(
            "Missing Skills:",
            ", ".join(rec["Missing Skills"])
        )

    print("\nRecommendation Complete.")


if __name__ == "__main__":
    main()