class JobApplicationScoring:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, experience_years, education_level, skills_count):
        """
        education_level: 1 - High School, 2 - Bachelor's, 3 - Master's, 4 - PhD
        skills_count: number of relevant skills
        """
        self.applicants.append({
            'name': name,
            'experience': experience_years,
            'education': education_level,
            'skills': skills_count
        })

    def calculate_score(self, applicant):
        """
        Scoring logic:
        - Experience: 2 points per year
        - Education: 10 points per level
        - Skills: 5 points per skill
        """
        score = (applicant['experience'] * 2) + (applicant['education'] * 10) + (applicant['skills'] * 5)
        return score

    def evaluate_applicants(self):
        results = []
        for applicant in self.applicants:
            score = self.calculate_score(applicant)
            results.append({'name': applicant['name'], 'score': score})
        return results


# =========================================
# Example Usage
# =========================================
if __name__ == "__main__":
    system = JobApplicationScoring()
    system.add_applicant("Alice", experience_years=5, education_level=3, skills_count=4)
    system.add_applicant("Bob", experience_years=2, education_level=2, skills_count=3)
    system.add_applicant("Charlie", experience_years=8, education_level=4, skills_count=5)

    evaluated = system.evaluate_applicants()

    print("Job Application Scores:")
    for result in evaluated:
        print(f"{result['name']}: {result['score']} points")
