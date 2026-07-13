import os

students = [
    {"name": "Eiliya", "scores": [20, 18, 17, 15]},
    {"name": "Alireza", "scores": [15, 14, 13, 12]}
]


def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")


def read():
    clear()
    for idx, student in enumerate(students):
        scores = list(map(lambda x: str(x), student['scores']))
        scores = ' - '.join(scores)
        print(f"{idx + 1} - Name: {student['name']} Score: {scores}")
        print("-" * 20)


def create():
    clear()
    name = input("Enter student name: ")
    scores = input("Enter scores (20, 28, 29): ")
    scores = [int(score.strip()) for score in scores.split(",")]
    students.append({
        "name": name,
        "scores": scores
    })
    print("Student created successfully!")


def update():
    clear()
    read()
    selected_index = int(input("Select student number to update: ")) - 1

    name = input("Enter student updated name: ")
    scores = input("Enter updated scores (20, 28, 29): ")
    scores = [int(score.strip()) for score in scores.split(",")]

    students[selected_index] = {
        "name": name,
        "scores": scores
    }
    print(f"Student {name} updated successfully!")


def delete():
    clear()
    read()
    selected_index = int(input("Select student number to delete: ")) - 1
    removed_item = students.pop(selected_index)
    print(f"Student {removed_item['name']} deleted successfully!")


def show_student_information():
    clear()
    read()
    selected_index = int(input("Select student number to update: ")) - 1
    data = students[selected_index]
    name = data["name"]
    scores = data["scores"]

    print(f"Student information for {name}:")
    print(f"Min score: {min(scores)}")
    print(f"Max score: {max(scores)}")
    print(f"Average score: {round(sum(scores) / len(scores), 2)}")
    results = list(map(lambda score: score > 17, scores))
    # results = [score > 17 for score in scores]
    print(f"A+ for all scores: {all(results)}")
    print(f"A for one score: {any(results)}")
    print('-' * 20)


def show_information():
    clear()

    print("All Students")
    avgs = [sum(s['scores']) / len(s['scores']) for s in students]
    for student, avg in zip(students, avgs):
        print(f"Student {student['name']} average score: {avg}")
    print("-" * 20)

    print("A+ Students")
    check = lambda s: round(sum(s['scores']) / len(s['scores']), 2) > 17
    filtered_students = list(filter(check, students))
    for student in filtered_students:
        print(f"Student {student['name']}")
    print("-" * 20)

    print("Top students")
    sorted_value = lambda s: round(sum(s['scores']) / len(s['scores']), 2)
    sorted_students = sorted(students, key=sorted_value, reverse=True)
    for student in sorted_students:
        print(f"Student {student['name']}")

    print("-" * 20)
    # reversed, abs


# print(students)
# print(avgs)


if __name__ == "__main__":
    read()
