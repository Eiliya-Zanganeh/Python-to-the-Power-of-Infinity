# import utils
# from utils import read, create
# from utils import *
import utils as ul


def main():
    print("Welcome to the student program!")

    while True:
        print("1 - Read all students")
        print("2 - Create new student")
        print("3 - Update student")
        print("4 - Delete student")
        print("5 - Show student information")
        print("6 - Show information")

        user_input = input("Enter your choice ( q for quit ): ")

        match user_input:
            case "1":
                ul.read()

            case "2":
                ul.create()

            case "3":
                ul.update()

            case "4":
                ul.delete()

            case "5":
                ul.show_student_information()

            case "6":
                ul.show_information()

            case _:
                break


if __name__ == "__main__":
    main()
