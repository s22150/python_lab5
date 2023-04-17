def calculate_grade(points):
    if points < 0 or points > 100:
        return "Nieprawidłowa liczba punktów"

    if points <= 50:
        return 2

    elif points <= 60:
        return 3

    elif points <= 70:
        return 3.5

    elif points <= 80:
        return 4

    elif points <= 90:
        return 4.5

    else:
        return 5


def write_to_file(students):
    with open('students.txt', 'w') as f:
        for email, student in students.items():
            f.write(
                f"{email},{student['first_name']},{student['last_name']},{student['points']},{student['final_grade']},{student['status']}\n")



import csv

students = {}

with open('students.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        email, first_name, last_name, points = row[:4]
        if email not in students:
            students[email] = {'first_name': first_name,
                               'last_name': last_name,
                               'points': points,
                               'final_grade': '',
                               'status': ''}
        if len(row) > 4:
            students[email]['final_grade'] = row[4]
        if len(row) > 5:
            students[email]['status'] = row[5]

while True:
    for email, student in students.items():
        print(email + " " + student['first_name'] + " " + student['last_name'] + " " , student['points'])
    print("menu\n 1.Dodaj studenta \n 2.Usun studenta \n 3.Wystaw ocene \n 4.Wyslij maila z ocena \n 5.Exit")
    match input("podaj opcje "):
        case "1":
            email = input("Enter student's email: ")
            if email in students:
                print("Error: Email already exists")
                continue

            name = input("Enter student's name: ")
            surname = input("Enter student's surname: ")
            points = float(input("Enter student's points: "))
            final_grade = calculate_grade(points)
            student = {
                'email': email,
                'first_name': name,
                'last_name': surname,
                'points': points,
                'final_grade': final_grade,
                'status': "GRADED"
            }
            students[email] = student
            print("Zostal dodany student " + name + " " + surname)
            write_to_file(students)
        case "2":
            for email,student in students.items():
                print(email + " " + student['first_name'] + " " + student["last_name"])
            mail = input("Wprowadz mail studenta ktorego chcesz usunac ")
            if not mail in students:
                print("Error: Email does not exist")
                continue
            del students[mail]
            print("Student zostal usuniety")
            write_to_file(students)
        case "3":
            for email, student in students.items():
                if not student['final_grade'] and student['status'] not in ['GRADED', 'MAILED']:
                    student['final_grade'] = calculate_grade(int(student['points']))
                    student['status'] = 'GRADED'
            for email, data in students.items():
                print(
                    f"{data['first_name']} {data['last_name']}: {data['points']} punktów, ocena końcowa: {data['final_grade']}, status: {data['status']}")
            write_to_file(students)
        case "4":
            for email,student in students.items():
                if student.get('status') != "MAILED":
                    print("Wysylam maila z ocena do " + student.get('first_name') + " " + student.get('last_name'))
                    student['status'] = "MAILED"
            write_to_file(students)
        case "5":
            quit()
