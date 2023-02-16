from src.domain.grade import Grade
from src.services.undo_service import Call, Operation, ComplexOperation
from src.services.validators import GradeValidator


class GradeService:
    def __init__(self,grade_repo,student_repo,discipline_repo,service_undo):
        self.__repository = grade_repo
        self.__student_repository = student_repo
        self.__discipline_repository = discipline_repo
        self.__undo = service_undo

    def initialize_grades(self):
        self.__repository.initialize_grades()

    def add_grade(self,student_id,discipline_id,grade_value):
        grade = Grade(student_id,discipline_id,grade_value)
        GradeValidator.validate_grade(grade)
        self.__repository.add_grade(grade)

        redo = Call(self.__repository.add_grade, grade)
        undo = Call(self.__repository.remove_grade, grade)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def remove_grade(self,grade):
        self.__repository.remove_grade(grade)
        undo = Call(self.__repository.add_grade, grade)
        redo = Call(self.__repository.remove_grade, grade)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def get_grades_list(self):
        return self.__repository.get_grades_list()

    def find_students_failing(self):
        students_list = self.__student_repository.get_students_list()
        disciplines_list = self.__discipline_repository.get_disciplines_list()
        grades_list = self.get_grades_list()
        failing_students_list = []
        for student in students_list:
            for discipline in disciplines_list:
                grades_sum = 0
                number_of_grades = 0
                for grade in grades_list:
                    if int(grade.student_id) == int(student.id) and int(grade.discipline_id) == int( discipline.id) :
                        grades_sum = grades_sum + int(grade.grade_value)
                        number_of_grades = number_of_grades + 1
                if number_of_grades > 0:
                    average_grade = float(grades_sum/number_of_grades)
                    if average_grade < 5:
                        failing_students_list.append(student)
        return failing_students_list
