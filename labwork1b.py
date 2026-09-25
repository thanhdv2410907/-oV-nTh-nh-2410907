
students = []
courses = []
marks = {}
def input_student_infor():
    sid = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Student DoB (dd/mm/yyyy): ")
    return(sid, name, dob)
def input_students():
    n = int(input("number of student: "))
    for i in range(n):
        print(f"--- student {i + 1} ---")
        students.append(input_student_infor())    

def input_course_infor():
    cid = input("Course ID: ")
    cname = input("course name: ")
    return(cid, cname)
def input_courses():
    n = int(input("number of course: "))
    for i in range(n):
        print(f"--- Course {i + 1} ---")
        courses.append(input_course_infor())

def input_marks():
    print("Courses: ")
    for c in courses:
        print(c[0], "--", c[1])
    cid = input("select course ID:")
    course_ids = [c[0] for c in courses]
    if cid not in course_ids:
        print(" course not found!")
        return
    if cid not in marks:
        marks[cid] = {}
    for s in students:
        mark = float(input(f"Mark of {s[1]} ({s[0]}): "))
        marks[cid][s[0]] = mark

def list_courses():
    print("--- Course ---")
    for c in courses:
        print(f"ID: {c[0]} --- Course name: {c[1]}")

def list_students():
    print("--- Student ---")
    for s in students:
        print(f"ID: {s[0]} --- Student name: {s[1]} --- DoB: {s[2]}")

def show_marks():
    list_courses()
    cid = input("--- Select course ID ---")
    if cid not in marks:
        print(" not marks for this course yet!")
        return 
    print(f"--- mark of course {cid} ---")
    for s in students:
        if s[0] in marks[cid]:
            print(f"{s[1]}: {marks[cid][s[0]]}")

def print_menu():
    print("\n===== STUDENT MARK MANAGEMENT =====")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks for a course")
    print("4. List students")
    print("5. List courses")
    print("6. Show marks of a course")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Your choice: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

main()