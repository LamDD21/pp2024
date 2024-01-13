 #lists and dictionary to store student and course information
students = []
courses = []
student_marks = {}

# Function to input the number of students in the class
def input_number_of_students():
    num_students = int(input("Enter number of students in the class: "))
    return num_students

# Function to input student information
def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return (student_id, student_name, student_dob)

# Function to input the number of courses
def input_number_of_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

# Function to input course information
def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

# Function to select a course and input marks for students in this course
def input_student_marks():
    course_id = input("Enter course ID to input marks for students: ")
    if course_id in courses:
        student_marks.setdefault(course_id, {})
        for student in students:
            student_id, student_name, _ = student
            mark = int(input(f"Enter mark for student {student_name} in course {course_id}: "))
            student_marks[course_id][student_id] = mark
    else:
        print("No Course")

# Function to list courses
def list_courses():
    print("List of courses:")
    for course_id, course_name in courses:
        print(f"Course ID: {course_id}, Course Name: {course_name}")

# Function to list students
def list_students():
    print("List of students:")
    for student_id, student_name, dob in students:
        print(f"Student ID: {student_id}, Student Name: {student_name}, Date of Birth: {dob}")

# Function to show student marks for a specific course
def show_student_marks_for_course():
    course_id = input("Enter course ID to show student marks: ")
    if course_id in student_marks:
        print(f"Student marks for course {course_id}:")
        for student_id, mark in student_marks[course_id].items():
            student_name = next((name for id, name, _ in students if id == student_id), "Unknown")
            print(f"Student ID: {student_id}, Student Name: {student_name}, Mark: {mark}")
    else:
        print("No marks")

# Main function to run the program
def main():
    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_information())

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_information())

    # Run the menu to choose the functionalities
    while True:
        print("\nChoose an option:")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            input_student_marks()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_student_marks_for_course()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
