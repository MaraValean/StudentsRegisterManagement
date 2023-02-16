class Student:
    def __init__(self,student_id,name):
        self.__id = student_id
        self.__name = name
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name = new_name
    def __str__(self):
        return "Id: " + str(self.id) + ", Student name:  " + self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other_student):
        if isinstance(other_student, Student) == False:
            return False
        return self.id == other_student.id

    @staticmethod
    def from_line(line):
        parts = line.split(",")
        student_id = parts[0]
        name = parts[1]
        return Student(student_id, name)

    @staticmethod
    def to_line(student):
        line = f"{str(student.__id)},{student.__name}"
        return line
