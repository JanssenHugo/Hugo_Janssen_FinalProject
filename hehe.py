""
Student Performance Tracker CLI System 

Module Description:
This program is a command-line interface (CLI) application that manages student records. # type: ignore
It allows users to add students, record scores, compute averages, search, sort, delete,
and save data using file handling (JSON).

This system demonstrates core Python programming concepts including:
- Object-Oriented Programming (Classes and Objects)
- Data Structures (Lists, Dictionaries, Sets, Tuples)
- Functions and Modular Programming
- File Handling (JSON read/write)
- Algorithms (Searching and Sorting)
- Input Validation and Error Handling

Author:JANSSEN,HUGO J.
Date: 2026
""

import json

CORE_SUBJECTS = {"Math", "Science", "English", "Programming"}


class Student:
    """Represents a student record."""

    def __init__(self, student_id, name):
        # Basic student information
        self.student_id = student_id
        self.name = name
        # DATA STRUCTURES USED:
        # LIST → stores (subject, score) pairs
        self.scores = []
        self.subjects = set()
# STEP 2: ADD SCORE PROCESS
    def add_score(self, subject, score):

 # Add subject into set (prevents duplicates)
        self.subjects.add(subject)
 # Store score as tuple 
        self.scores.append((subject, score))

    def average(self):
        if not self.scores:
            return 0

        total = sum(score for _, score in self.scores)
        return total / len(self.scores)

    def __str__(self):
        return f"{self.student_id} | {self.name} | Average: {self.average():.2f}"


class Tracker:
    """Handles student operations."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def search_student(self, keyword):
        return [
            s for s in self.students.values()
            if keyword.lower() in s.name.lower()
        ]

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

    def sort_students(self):
        return sorted(
            self.students.values(),
            key=lambda x: x.average(),
            reverse=True
        )

    def save_file(self, filename="students.json"):
        data = []

        for student in self.students.values():
            data.append({
                "id": student.student_id,
                "name": student.name,
                "subjects": list(student.subjects),
                "scores": student.scores
            })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)


def display_menu():
    print("\n===== STUDENT PERFORMANCE TRACKER =====")
    print("1. Add Student")
    print("2. Add Score")
    print("3. View Students")
    print("4. Search")
    print("5. Sort by Average")
    print("6. Delete Student")
    print("7. View Core Subjects")
    print("8. View Student Subjects")
    print("9. Save")
    print("10. Exit")


def demo(tracker):
    s1 = Student("001", "Janssen")
    s1.add_score("Math", 95)
    s1.add_score("Science", 89)

    s2 = Student("002", "Kyle")
    s2.add_score("English", 80)

    tracker.add_student(s1)
    tracker.add_student(s2)

    for student in tracker.sort_students():
        print(student)


def run_cli():
    tracker = Tracker()

    while True:
        display_menu()

        try:
            choice = input("Enter choice: ")
        except (EOFError, OSError):
            print("Interactive input unavailable")
            demo(tracker)
            break

        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            tracker.add_student(Student(sid, name))
            print("Student added")

        elif choice == "2":
            sid = input("Student ID: ")

            if sid in tracker.students:
                print("Choose Subject")
                print("1. Math")
                print("2. Science")
                print("3. English")
                print("4. Programming")

                subject_choice = input("Subject Number: ")

                subject_map = {
                    "1": "Math",
                    "2": "Science",
                    "3": "English",
                    "4": "Programming"
                }

                if subject_choice not in subject_map:
                    print("Invalid subject choice")
                    continue

                subject = subject_map[subject_choice]

                try:
                    score = float(input("Score: "))
                except ValueError:
                    print("Invalid score")
                    continue

                tracker.students[sid].add_score(subject, score)
                print("Score added")
            else:
                print("Student not found")

        elif choice == "3":
            for student in tracker.students.values():
                print(student)

        elif choice == "4":
            keyword = input("Search: ")
            results = tracker.search_student(keyword)

            if results:
                for student in results:
                    print(student)
            else:
                print("No student found")

        elif choice == "5":
            for student in tracker.sort_students():
                print(student)

        elif choice == "6":
            sid = input("Enter ID to delete: ")

            if tracker.delete_student(sid):
                print("Student deleted")
            else:
                print("Student not found")

        elif choice == "7":
            for subject in sorted(CORE_SUBJECTS):
                print("-", subject)

        elif choice == "8":
            sid = input("Student ID: ")

            if sid in tracker.students:
                student = tracker.students[sid]
                if student.subjects:
                    for subject in sorted(student.subjects):
                        print("-", subject)
                else:
                    print("No subjects yet")
            else:
                print("Student not found")

        elif choice == "9":
            tracker.save_file()
            print("Saved to file")

        elif choice == "10":
            print("Goodbye")
            break

        else:
            print("Invalid input")


s = Student("100", "Test")
s.add_score("Programming", 90)
s.add_score("Math", 100)
assert round(s.average(), 2) == 95.00

tracker_test = Tracker()
tracker_test.add_student(s)
assert len(tracker_test.search_student("test")) == 1
assert tracker_test.delete_student("100") is True
assert len(tracker_test.students) == 0


if __name__ == "__main__":
    run_cli()
