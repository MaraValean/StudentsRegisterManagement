from src.exceptions import *


class Ui:
    def __init__(self, service_discipline, service_student,service_grade, service_undo):
        self.__discipline_service = service_discipline
        self.__student_service = service_student
        self.__grade_service = service_grade
        self.__undo_service = service_undo

    def print_disciplines_list(self):
        disciplines_list = self.__discipline_service.get_disciplines_list()
        for discipline in disciplines_list:
            print(str(discipline))

    def print_students_list(self):
        students_list = self.__student_service.get_students_list()
        for student in students_list:
            print(str(student))

    def print_grades_list(self):
        grades_list = self.__grade_service.get_grades_list()
        for grade in grades_list:
            print(str(grade))

    def add_discipline(self):
        discipline_id = input("Type in discipline id> ")
        name = input("Type in discipline name> ")
        try:
            self.__discipline_service.add_new_discipline(discipline_id, name)
            print("Discipline added successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def add_student(self):
        student_id = input("Type in student id> ")
        name = input("Type in student name> ")
        try:
            self.__student_service.add_new_student(student_id, name)
            print("Student added successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def add_grade(self):
        student_id = input("Type in student id> ")
        discipline_id = input("Type in discipline id> ")
        grade_value = input("Type in grade> ")
        try:
            self.__grade_service.add_grade(student_id, discipline_id,grade_value)
            print("Grade added successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def update_discipline(self):
        discipline_id = input("Type in discipline id> ")
        new_name = input("Type in new discipline name> ")
        try:
            self.__discipline_service.update_discipline(discipline_id, new_name)
            print("Discipline updated successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def update_student(self):
        student_id = input("Type in student id> ")
        new_name = input("Type in new student name> ")
        try:
            self.__student_service.update_student(student_id,new_name)
            print("Student updated successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def remove_discipline(self):
        discipline_id = input("Type in discipline id> ")

        try:
            self.__discipline_service.remove_discipline(discipline_id)
            print("Discipline removed successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def remove_student(self):
        student_id = input("Type in student id> ")

        try:
            self.__student_service.remove_student(student_id)
            print("Student removed successfully!")
        except ValidatorException as ve:
            print(ve)
        except RepositoryException as re:
            print(re)

    def search_discipline(self):
        search_input = input("Search for a discipline> ")
        found_disciplines = self.__discipline_service.search_discipline(search_input)
        if len(found_disciplines) == 0:
            print("No discipline found")
        else:
            for discipline in found_disciplines:
                print(str(discipline))

    def search_student(self):
        search_input = input("Search for a student> ")
        found_students = self.__student_service.search_student(search_input)
        if len(found_students) == 0:
            print("No student found")
        else:
            for student in found_students:
                print(str(student))

    def print_students_sorted_by_average_grade(self):
        number_of_students_to_display = int(input("Enter the number of students you want to see> "))
        students_list_sorted = self.__student_service.create_students_sorted_by_average_grade()
        for i in range(number_of_students_to_display):
            print(str(students_list_sorted[i]))

    def print_disciplines_sorted_by_average_grade(self):
        disciplines_list_sorted = self.__discipline_service.disciplines_sorted_by_average_grade()
        for discipline in disciplines_list_sorted:
            print(str(discipline))

    def print_students_failing(self):
        failing_students_list = self.__grade_service.find_students_failing()
        for student in failing_students_list:
            print(str(student))

    def undo_operation(self):
        try:
            self.__undo_service.undo()
            print("Undo operation done successfully!")
        except UndoException as ue:
            print(ue)

    def redo_operation(self):
        try:
            self.__undo_service.redo()
            print("Redo operation done successfully!")
        except UndoException as ue:
            print(ue)

    @staticmethod
    def print_menu():
        print("STUDENTS REGISTER MANAGEMENT")
        print("0. exit ")
        print("1. display students list")
        print("2. add student")
        print("3. remove student")
        print("4. update student")
        print("5. display disciplines list")
        print("6. add discipline")
        print("7. remove discipline")
        print("8. update discipline")
        print("9. add grade")
        print("10. display grades list")
        print("11. search student")
        print("12. search discipline")
        print("13. display failing students")
        print("14. display students with best school situation")
        print("15. display disciplines sorted")
        print("16. undo last operation")
        print("17. redo last operation")

    def start(self):
        self.__student_service.initialize_students()
        self.__discipline_service.initialize_disciplines()
        self.__grade_service.initialize_grades()
        while True:
            self.print_menu()
            user_option = input("plese select what you want to do> ")
            if user_option == "1":
                self.print_students_list()
            elif user_option == "2":
                self.add_student()
            elif user_option == "3":
                self.remove_student()
            elif user_option == "4":
                self.update_student()
            elif user_option == "5":
                self.print_disciplines_list()
            elif user_option == "0":
                exit()
            elif user_option == "6":
                self.add_discipline()
            elif user_option == "7":
                self.remove_discipline()
            elif user_option == "8":
                self.update_discipline()
            elif user_option == "9":
                self.add_grade()
            elif user_option == "10":
                self.print_grades_list()
            elif user_option == "11":
                self.search_student()
            elif user_option == "12":
                self.search_discipline()
            elif user_option == "13":
                self.print_students_failing()
            elif user_option == "14":
                self.print_students_sorted_by_average_grade()
            elif user_option == "15":
                self.print_disciplines_sorted_by_average_grade()
            elif user_option == "16":
                self.undo_operation()
            elif user_option == "17":
                self.redo_operation()
            else:
                print("invalid command")


