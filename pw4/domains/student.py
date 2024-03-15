class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_gpa(self, courses):
        total_marks = 0
        total_credits = 0
        for course_id, mark in self.marks.items():
            for course in courses:
                if course.course_id == course_id:
                    total_marks += mark * course.credits
                    total_credits += course.credits
                    break
        if total_credits > 0:
            return total_marks / total_credits
        else:
            return 0
