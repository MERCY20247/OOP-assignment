
    # QUESTIONS
    # 1) Add a constructor for the cohort class
    # 2) Add a method to the class that prints the cohort name, and the total number of students
    # 3) Create a new instance of the cohort class.

    #SOLUTIONS
    # 1)
class Cohort4:
    def __init__(self, name, description, start_date, end_date, students=None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

        self.students = students if students is not None else []

    def print_cohort_info(self):
    # 2)
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of Students: {len(self.students)}")

# 3)
cohort = Cohort4(
    name="Cohort 4",
    description="This is a Python Class 2024.",
    start_date="2024-08-20",
    end_date="2026-12-12",
    students=["Mercy", "Angel", "Nicole", "Ethan"]
)

cohort.print_cohort_info()
