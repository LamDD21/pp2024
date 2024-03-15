from domains.student import Student
from domains.course import Course
from input import *
from output import *

class Information:
    def __init__(self):
        self.students = []
        self.courses = []
        self.student_marks = {}

    # Implement other Information class functions

if __name__ == "__main__":
    school_system = Information()
    school_system.main()
