import pickle

from src.domain.student import Student
from src.exceptions import RepositoryException


class StudentRepository:
    def __init__(self):
        self._students_list = []

    def initialize_students(self):
        self._students_list = []
        name = ["Andrei Balcescu", "Andreea Pop", "Adela Petrescu", "Viorel Drimus", "Remus Rus", "Florin Moldovan",
                "Sebastian Joicaliuc",
                "Raul Treista", "Mariana Stan", "Ionela Teleptean", "Rares Simedrea", "Cosmin Ardelean", "Vasile Osan",
                "Alex Velea",
                "Catalin Bolo", "Petrisor Vlad", "Florin Boc", "Emilia Mutu", "Ioana Ieudean", "Mark Zoltan"]
        for i in range(20):
            self._students_list.append(Student(i + 1, name[i]))

    def find_student_in_students_list(self, student_id):
        student_index = 0
        for other_student in self._students_list:
            if int(other_student.id) == int(student_id):
                return student_index
            student_index = student_index + 1
        return - 1

    def add_new_student(self, student):
        if self.find_student_in_students_list(student.id) != -1:
            raise RepositoryException("Element having id=" + str(student.id) + " already stored!")
        self._students_list.append(student)

    def remove_student(self, student_id):
        student_index = self.find_student_in_students_list(student_id)
        if student_index == -1:
            raise RepositoryException("student doesn't exist!")
        del self._students_list[student_index]

    def update_student(self,student_id,new_name):
        student_index = self.find_student_in_students_list(student_id)
        if student_index == -1:
            raise RepositoryException("student doesn't exist!")
        student = self._students_list[student_index]
        student.set_name(new_name)

    def get_students_list(self):
        return self._students_list

    def __len__(self):
        return len(self._students_list)


class StudentFileRepository(StudentRepository):

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Student.from_line
        self.__write_function = Student.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'r') as file:
            self._students_list.clear()
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if len(line):  # to avoid reading the last empty line
                    entity = self.__read_function(line)
                    self._students_list.append(entity)

    def __write_all_to_file(self):
        with open(self.__file_path, 'w') as file:
            for entity in self._students_list:
                file.write(self.__write_function(entity) + '\n')

    def __append_to_file(self, entity):
        with open(self.__file_path, 'a') as file:
            file.write('\n' + self.__write_function(entity) + '\n')

    def __len__(self):
        self.__read_all_from_file()
        return super().__len__()

    def initialize_students(self):
        pass

    def add_new_student(self, entity):
        self.__read_all_from_file()
        super().add_new_student( entity)
        self.__append_to_file(entity)

    def remove_student(self, entity_id):
        self.__read_all_from_file()
        super().remove_student( entity_id)
        self.__write_all_to_file()

    def update_student(self, entity_id, entity_name):
        self.__read_all_from_file()
        super().update_student( entity_id, entity_name)
        self.__write_all_to_file()

    def find_student_in_students_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_student_in_students_list( entity_id)

    def get_students_list(self):
        self.__read_all_from_file()
        return super().get_students_list()


class StudentBinaryRepository(StudentRepository):

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_function = Student.from_line
        self.__write_function = Student.to_line
        super().__init__()

    def __read_all_from_file(self):
        with open(self.__file_path, 'rb') as file:
            self._students_list.clear()
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

    def __len__(self):
        self.__read_all_from_file()
        return super().__len__()

    def initialize_students(self):
        pass

    def add_new_student(self, entity):
        self.__read_all_from_file()
        super().add_new_student( entity)
        self.__append_to_file(entity)

    def remove_student(self, entity_id):
        self.__read_all_from_file()
        super().remove_student( entity_id)
        self.__write_all_to_file()

    def update_student(self, entity_id, entity_name):
        self.__read_all_from_file()
        super().update_student( entity_id, entity_name)
        self.__write_all_to_file()

    def find_student_in_students_list(self, entity_id):
        self.__read_all_from_file()
        return  super().find_student_in_students_list( entity_id)

    def get_students_list(self):
        self.__read_all_from_file()
        return super().get_students_list()