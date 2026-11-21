import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from domain import *

def main_menu():
    print("=== Online Learning Platform CLI ===")
    inst = Instructor(1, "prof@uni.edu", "Dr. Smith", "Math Expert")
    inst.approve()
    course = Course("MATH101", "Calculus I", inst, 99.99)
    mod1 = Module("Introduction")
    mod1.add_lesson(Lesson("Limits", 45))
    mod1.add_lesson(Lesson("Derivatives", 60))
    course.add_module(mod1)
    student = Student(2, "jane@email.com", "Jane Doe", "S12345")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Course Info")
        print("2. Enroll in Course")
        print("3. Complete a Lesson")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print(f"\nCourse: {course.title} | Price: ${course.price} | Duration: {course.calculate_total_duration()} mins")
        elif choice == "2":
            enrollment = Enrollment(student, course)
            student.enroll(course, enrollment)
            print("Successfully enrolled!")
        elif choice == "3":
            if not student.enrollments:
                print("You must enroll first!")
                continue
            enr = student.enrollments[0]
            first_lesson = course.modules[0].lessons[0]
            enr.complete_lesson(first_lesson)
            print(f"Lesson completed! Current progress: {enr.progress}%")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()