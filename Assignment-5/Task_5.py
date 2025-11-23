# Inclusive Job Application Scoring System

class InclusiveJobScoring:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, gender, experience, education, skills):
        # Gender is stored but NOT used in scoring
        self.applicants.append({
            'name': name,
            'gender': gender,  # can be 'Male', 'Female', 'Non-binary', 'Other'
            'experience': experience,
            'education': education,
            'skills': skills
        })

    def calculate_score(self, applicant):
        # Scoring: experience=2 pts/year, education=10 pts/level, skills=5 pts each
        return applicant['experience']*2 + applicant['education']*10 + applicant['skills']*5

    def evaluate_applicants(self):
        results = []
        for applicant in self.applicants:
            score = self.calculate_score(applicant)
            results.append({'name': applicant['name'], 'score': score})
        return results

# ===================== Example Usage =====================
if __name__ == "__main__":
    system = InclusiveJobScoring()
    system.add_applicant("Alice", "Female", 5, 3, 4)
    system.add_applicant("Bob", "Male", 4, 2, 5)
    system.add_applicant("Charlie", "Non-binary", 6, 4, 3)
    system.add_applicant("Alex", "Other", 3, 3, 5)  # Gender-neutral example

    evaluated = system.evaluate_applicants()
    print("Inclusive Job Application Scores:")
    for result in evaluated:
        print(f"{result['name']}: {result['score']} points")
