
class Grade:
    def __init__(self,student_id, discipline_id, grade_value):
        self.__student_id = student_id
        self.__discipline_id = discipline_id
        self.__grade_value = grade_value
    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    def set_student_id(self,student_id):
        self.__student_id = student_id

    def set_discipline_id(self,discipline_id):
        self.__discipline_id = discipline_id

    def set_grade_value(self,grade_value):
        self.__grade_value = grade_value

    def __str__(self):
        return "student id: " + str(self.__student_id) + ", discipline id:  " + self.__discipline_id + " , grade: " + self.__grade_value

    def __repr__(self):
        return str(self)

    @staticmethod
    def from_line(line):
        parts = line.split(",")
        student_id = parts[0]
        discipline_id = parts[1]
        grade_value = parts[2]
        return Grade(student_id, discipline_id, grade_value)

    @staticmethod
    def to_line(grade):
        line = f" {str(grade.__student_id)}{str(grade.__discipline_id)},{grade.__grade_value}"
        return line

