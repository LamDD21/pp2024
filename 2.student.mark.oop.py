class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class Information:
    def __init__(self):
        self.students = []
        self.courses = []
        self.student_marks = {}

    def input_number_of_students(self):
        num_students = int(input("Enter number of students in the class: "))
        return num_students

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        return Student(student_id, student_name, student_dob)

    def input_number_of_courses(self):
        num_courses = int(input("Enter number of courses: "))
        return num_courses

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_student_marks(self):
        course_id = input("Enter course ID to input marks for students: ")
        if course_id in [course.course_id for course in self.courses]:
            self.student_marks.setdefault(course_id, {})
            for student in self.students:
                mark = int(input(f"Enter mark for student {student.student_name} in course {course_id}: "))
                self.student_marks[course_id][student.student_id] = mark
        else:
            print("No Course")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"Student ID: {student.student_id}, Student Name: {student.student_name}, Date of Birth: {student.student_dob}")

    def show_student_marks_for_course(self):
        course_id = input("Enter course ID to show student marks: ")
        if course_id in self.student_marks:
            print(f"Student marks for course {course_id}:")
            for student_id, mark in self.student_marks[course_id].items():
                student = next((s for s in self.students if s.student_id == student_id), None)
                if student:
                    print(f"Student ID: {student_id}, Student Name: {student.student_name}, Mark: {mark}")
                else:
                    print(f"Student ID: {student_id}, Student Name: Unknown, Mark: {mark}")
        else:
            print("No marks")

    def main(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            self.students.append(self.input_student_information())

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            self.courses.append(self.input_course_information())

        while True:
            print("\nChoose an option:")
            print("1. Input marks for a course")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.input_student_marks()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_student_marks_for_course()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    school_system = Information()
    school_system.main()
