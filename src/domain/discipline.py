class Discipline:
    def __init__(self, discipline_id, name):
        self.__id = discipline_id
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
        return "Id: " + str(self.id) + ", Discipline name:  " + self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other_discipline):
        if isinstance(other_discipline, Discipline) == False:
            return False
        return self.id == other_discipline.id

    @staticmethod
    def from_line(line):
        parts = line.split(",")
        discipline_id = parts[0]
        name = parts[1]
        return Discipline(discipline_id, name)

    @staticmethod
    def to_line(discipline):
        line = f"{str(discipline.__discipline_id)},{discipline.__name}"
        return line

