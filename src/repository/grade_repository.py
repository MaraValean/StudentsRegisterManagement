import pickle

from src.exceptions import RepositoryException
from src.domain.grade import Grade


class GradeRepository:
    def __init__(self):
        self._grades_list =[]

    def initialize_grades(self):
        id_stud = ["11","2", "3", "4", "11", "9", "2",  "6", "1", "8"]
        id_disc = ["9", "10", "4", "2", "3", "1", "10", "7", "2", "11"]
        grade_value = ["10", "5", "2", "9", "4", "10", "4", "3", "9", "4"]
        for i in range(10):
            grade = Grade(id_stud[i], id_disc[i], grade_value[i])
            self._grades_list.append(grade)

    def find_grade_in_grades_list(self,grade):
        grade_index = 0
        for other_grade in self._grades_list:
            if int(grade.grade_value) == int(other_grade.grade_value) and int(grade.discipline_id) == int(other_grade.discipline_id) and int(grade.student_id) == int(other_grade.student_id):
                return grade_index
            grade_index = grade_index + 1
        return -1

    def add_grade(self,grade):
        self._grades_list.append(grade)

    def remove_grade(self,grade):
        grade_index= self.find_grade_in_grades_list(grade)
        if grade_index == -1 :
            raise RepositoryException("grade doesn't exist!")
        del self._grades_list[grade_index]

    def get_grades_list(self):
        return self._grades_list


class GradeFileRepository(GradeRepository):

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Grade.from_line
        self.__write_function = Grade.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'r') as file:
            self._grades_list .clear()
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if len(line):  # to avoid reading the last empty line
                    entity = self.__read_function(line)
                    self._grades_list.append(entity)

    def __write_all_to_file(self):
        with open(self.__file_path, 'w') as file:
            for entity in self._grades_list :
                file.write(self.__write_function(entity) + '\n')

    def __append_to_file(self, entity):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._grades_list, file)

    def add_grade(self, entity):
        self.__read_all_from_file()
        super().add_grade(entity)
        self.__append_to_file(entity)

    def remove_grade(self, entity_id):
        self.__read_all_from_file()
        super().remove_grade( entity_id)
        self.__write_all_to_file()

    def find_grade_in_grades_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_grade_in_grades_list( entity_id)

    def get_disciplines_list(self):
        self.__read_all_from_file()
        return  super().get_grades_list()


class GradeBinaryRepository(GradeRepository):

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Grade.from_line
        self.__write_function = Grade.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'rb') as file:
            self._grades_list.clear()
            try:
                self._students_list = pickle.load(file)
            except EOFError:
                pass

    def __write_all_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._students_list, file)

    def __append_to_file(self, entity):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._students_list, file)



    def add_grade(self, entity):
        self.__read_all_from_file()
        super().add_grade(entity)
        self.__append_to_file(entity)

    def remove_grade(self, entity_id):
        self.__read_all_from_file()
        super().remove_grade( entity_id)
        self.__write_all_to_file()

    def find_grade_in_grades_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_grade_in_grades_list( entity_id)

    def get_disciplines_list(self):
        self.__read_all_from_file()
        return  super().get_grades_list()

