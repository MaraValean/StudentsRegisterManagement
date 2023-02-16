from src.domain.discipline import Discipline
from src.services.undo_service import Call,Operation,ComplexOperation
from src.services.validators import DisciplineValidator
from src.exceptions import ValidatorException


class DisciplineService:
    def __init__(self, discipline_repo,grade_repo,service_undo):
        self.__repository = discipline_repo
        self.__grade_repository = grade_repo
        self.__undo = service_undo

    def add_new_discipline(self , discipline_id,name):

        discipline = Discipline(discipline_id,name)
        DisciplineValidator.validate_discipline(discipline)
        self.__repository.add_new_discipline(discipline)

        redo = Call(self.__repository.add_new_discipline, discipline)
        undo = Call(self.__repository.remove_discipline,discipline_id)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def update_discipline(self,discipline_id,new_name):
        discipline = Discipline(discipline_id, new_name)
        DisciplineValidator.validate_discipline(discipline)
        index = self.__repository.find_discipline_in_disciplines_list(discipline_id)
        disciplines_list = self.__repository.get_disciplines_list()
        old_name = disciplines_list[index].name
        self.__repository.update_discipline(discipline_id,new_name)

        undo = Call(self.__repository.update_discipline, discipline_id,old_name)
        redo = Call(self.__repository.update_discipline, discipline_id, new_name)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def remove_discipline(self,discipline_id):
        if discipline_id.isnumeric()==False:
            raise ValidatorException("Discipline id must be an integer")
        self.__repository.remove_discipline(discipline_id)
        grades_list = self.__grade_repository.get_grades_list()
        for grade in grades_list:
            if int(grade.discipline_id) == int(discipline_id):
                self.__grade_repository.remove_grade(grade)

        index = self.__repository.find_discipline_in_disciplines_list(discipline_id)
        disciplines_list = self.__repository.get_disciplines_list()
        discipline_name = disciplines_list[index].name
        discipline = Discipline(discipline_id, discipline_name)
        undo = Call(self.__repository.add_new_discipline, discipline)
        redo = Call(self.__repository.remove_discipline, discipline_id)
        operation = [Operation(undo, redo)]
        self.__undo.record(ComplexOperation(operation))

    def initialize_disciplines(self):
        self.__repository.initialize_disciplines()

    def get_disciplines_list(self):
        disciplines = self.__repository.get_disciplines_list()
        return disciplines

    def search_discipline(self,search_input):
        search_input = search_input.strip().lower()
        found_disciplines = []
        for discipline in self.__repository.get_disciplines_list():
            if search_input in str(discipline.id) or search_input in discipline.name.lower():
                found_disciplines.append(discipline)
        return found_disciplines

    @staticmethod
    def swap_disciplines(disciplines_list ,discipline, other_discipline ):
        disciplines_list[discipline], disciplines_list[other_discipline] = disciplines_list[other_discipline] , disciplines_list[discipline]
        return disciplines_list

    def disciplines_sorted_by_average_grade(self):
        disciplines_list = self.__repository.get_disciplines_list()
        for i in range(len(disciplines_list)):
            discipline_id = disciplines_list[i].id
            average_grade = self.calculate_average_grades(discipline_id)
            for j in range(i+1, len(disciplines_list)):
                if average_grade < self.calculate_average_grades(disciplines_list[j].id):
                    disciplines_list = self.swap_disciplines(disciplines_list, i, j)
        return disciplines_list

    def calculate_average_grades(self,discipline_id):
        grades_sum = 0
        number_of_grades = 0
        grades_list = self.__grade_repository.get_grades_list()
        for grade in grades_list:
            if int(grade.discipline_id) == int(discipline_id):
                grades_sum = grades_sum + int(grade.grade_value)
                number_of_grades = number_of_grades + 1
        if number_of_grades == 0:
            return 0
        else:
            average_grade = float(grades_sum / number_of_grades)
        return average_grade
