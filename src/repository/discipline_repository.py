import pickle

from src.domain.discipline import Discipline
from src.exceptions import RepositoryException


class DisciplineRepository:
    def __init__(self):
        self._disciplines_list = []

    def initialize_disciplines(self):
        name = ["Math", "Computer System Architecture", "Algebra", "Calculus", "Computational Logic",
                "Fundamentals of Programming", "Sport", "Phisics", "Chemistry", "English", "Romanian", "Biology"]
        for i in range(12):
            self._disciplines_list.append(Discipline(i + 1, name[i]))

    def find_discipline_in_disciplines_list(self,discipline_id):
        discipline_index = 0
        for other_discipline in self._disciplines_list:
            if int(other_discipline.id) == int(discipline_id):
                return discipline_index
            discipline_index = discipline_index + 1
        return -1

    def add_new_discipline(self, discipline):
        if self.find_discipline_in_disciplines_list(discipline.id) != -1:
            raise RepositoryException("Element having id=" + str(discipline.id) + " already stored!")
        self._disciplines_list.append(discipline)

    def remove_discipline(self,discipline_id):
        discipline_index = self.find_discipline_in_disciplines_list(discipline_id)
        if discipline_index == -1:
            raise RepositoryException("Discipline doesn't exist!")
        del self._disciplines_list[discipline_index]

    def update_discipline(self,discipline_id,new_name):
        discipline_index = self.find_discipline_in_disciplines_list(discipline_id)
        if discipline_index == -1:
            raise RepositoryException("Discipline doesn't exist!")
        discipline = self._disciplines_list[discipline_index]
        discipline.set_name(new_name)

    def get_disciplines_list(self):
        return self._disciplines_list

    def __len__(self):
        return len(self._disciplines_list)

    def __str__(self):
        string_row = ""
        for element in self._disciplines_list:
            string_row += str(element)
            string_row += "\n"
        return string_row


class DisciplineFileRepository(DisciplineRepository):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Discipline.from_line
        self.__write_function = Discipline.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'r') as file:
            self._disciplines_list .clear()
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if len(line):  # to avoid reading the last empty line
                    entity = self.__read_function(line)
                    self._disciplines_list.append(entity)

    def __write_all_to_file(self):
        with open(self.__file_path, 'w') as file:
            for entity in self._disciplines_list :
                file.write(self.__write_function(entity) + '\n')

    def __append_to_file(self, entity):
        with open(self.__file_path, 'a') as file:
            file.write('\n' + self.__write_function(entity) + '\n')

    def initialize_disciplines(self):
        pass

    def __len__(self):
        self.__read_all_from_file()
        return  super().__len__()

    def add_new_discipline(self, entity):
        self.__read_all_from_file()
        super().add_new_discipline( entity)
        self.__append_to_file(entity)

    def remove_discipline(self, entity_id):
        self.__read_all_from_file()
        super().remove_discipline( entity_id)
        self.__write_all_to_file()

    def update_discipline(self, entity_id,entity_name):
        self.__read_all_from_file()
        super().update_discipline( entity_id,entity_name)
        self.__write_all_to_file()

    def find_discipline_in_disciplines_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_discipline_in_disciplines_list( entity_id)

    def get_disciplines_list(self):
        self.__read_all_from_file()
        return  super().get_disciplines_list()


class DisciplineBinaryRepository(DisciplineRepository):

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Discipline.from_line
        self.__write_function = Discipline.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'rb') as file:
            self._disciplines_list.clear()
            try:
                self._students_list = pickle.load(file)
            except EOFError:
                pass

    def __write_all_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._disciplines_list, file)

    def __append_to_file(self, entity):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._disciplines_list, file)

    def initialize_disciplines(self):
        pass

    def __len__(self):
        self.__read_all_from_file()
        return  super().__len__()

    def add_new_discipline(self, entity):
        self.__read_all_from_file()
        super().add_new_discipline( entity)
        self.__append_to_file(entity)

    def remove_discipline(self, entity_id):
        self.__read_all_from_file()
        super().remove_discipline( entity_id)
        self.__write_all_to_file()

    def update_discipline(self, entity_id,entity_name):
        self.__read_all_from_file()
        super().update_discipline( entity_id,entity_name)
        self.__write_all_to_file()

    def find_discipline_in_disciplines_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_discipline_in_disciplines_list( entity_id)

    def get_disciplines_list(self):
        self.__read_all_from_file()
        return  super().get_disciplines_list()

