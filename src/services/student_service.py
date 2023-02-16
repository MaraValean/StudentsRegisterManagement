from src.domain.student import Student
from src.services.validators import StudentValidator
from src.exceptions import ValidatorException
from src.services.undo_service import Call,Operation,ComplexOperation


class StudentService:

    def __init__(self,student_repo,grade_repo,service_undo):
        self.__repository = student_repo
        self.__grade_repository = grade_repo
        self.__undo = service_undo

    def initialize_students(self):
        self.__repository.initialize_students()

    def add_new_student(self , student_id,name):
        student = Student(student_id,name)
        StudentValidator.validate_student(student)
        self.__repository.add_new_student(student)

        redo = Call(self.__repository.add_new_student, student)
        undo = Call(self.__repository.remove_student, student_id)
        operation = [Operation(undo , redo)]
        self.__undo.record(ComplexOperation(operation))

    def remove_student(self, student_id):
        if student_id.isnumeric() == False:
            raise ValidatorException("Discipline id must be an integer")
        index = self.__repository.find_student_in_students_list(student_id)
        students_list = self.__repository.get_students_list()
        # student_id = students_list[index].id
        student_name = students_list[index].name
        student_undo = Student(student_id, student_name)
        self.__repository.remove_student(student_id)

        undo = Call(self.__repository.add_new_student, student_undo)
        redo = Call(self.__repository.remove_student, student_id)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def update_student(self,student_id, new_name):
        student = Student(student_id, new_name)
        StudentValidator.validate_student(student)
        index = self.__repository.find_student_in_students_list(student_id)
        students_list = self.__repository.get_students_list()
        old_name = students_list[index].name
        self.__repository.update_student(student_id, new_name)


        undo = Call(self.__repository.update_student, student_id, old_name)
        redo = Call(self.__repository.update_student, student_id, new_name)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def get_students_list(self):
        return self.__repository.get_students_list()

    def search_student(self, search_input):
        search_input = search_input.strip().lower()
        found_students = []
        for student in self.__repository.get_students_list():
            if search_input in str(student.id) or search_input in student.name.lower():
                found_students.append(student)
        return found_students

    @staticmethod
    def swap_students(students_list ,student, other_student ):
        students_list[student], students_list[other_student] = students_list[other_student], students_list[student]
        return students_list

    def create_students_sorted_by_average_grade(self):
        students_list = self.__repository.get_students_list()
        for i in range(len(students_list)):
            student_id = students_list[i].id
            average_grade = self.calculate_average_grades(student_id)
            for j in range(i+1, len(students_list)):
                if average_grade < self.calculate_average_grades(students_list[j].id):
                    students_list = self.swap_students(students_list, i, j)
        return students_list

    def calculate_average_grades(self,student_id):
        grades_sum = 0
        number_of_grades = 0
        grades_list = self.__grade_repository.get_grades_list()
        for grade in grades_list:
            if int(grade.student_id) == int(student_id):
                grades_sum = grades_sum + int(grade.grade_value)
                number_of_grades = number_of_grades + 1
        if number_of_grades == 0 :
            return 0
        else:
            average_grade = float(grades_sum / number_of_grades)
        return average_grade
