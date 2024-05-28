class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def __str__(self):
        course_names = [course.course_name for course in self.enrolled_courses]
        return f"Student ID: {self.student_id}, Name: {self.name}, Enrolled Courses: {', '.join(course_names)}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        student_names = [student.name for student in self.students]
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Students: {', '.join(student_names)}"


class Enrollment:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)

    def add_course(self, course_id, course_name):
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, course_name)

    def enroll_student(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.enroll(course)

    def get_students_in_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            return course.students

    def get_courses_for_student(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            return student.enrolled_courses


def main():
    enrollment_system = Enrollment()
    
    # Adding students
    enrollment_system.add_student(1, "G.Mustafa")
    enrollment_system.add_student(2, "Adnan Khadim")
    
    # Adding courses
    enrollment_system.add_course(101, "Mathematics")
    enrollment_system.add_course(102, "Physics")
    
    # Enrolling students in courses
    enrollment_system.enroll_student(1, 101)
    enrollment_system.enroll_student(1, 102)
    enrollment_system.enroll_student(2, 101)
    
    # Display students in a course
    students_in_math = enrollment_system.get_students_in_course(101)
    print("Students in Mathematics:")
    for student in students_in_math:
        print(student)
    
    # Display courses for a student
    courses_for_alice = enrollment_system.get_courses_for_student(1)
    print("\nCourses for G.Mustafa:")
    for course in courses_for_alice:
        print(course)

if __name__ == "__main__":
    main()
