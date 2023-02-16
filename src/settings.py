from src.repository.student_repository import StudentRepository, StudentFileRepository, StudentBinaryRepository
from src.repository.discipline_repository import DisciplineRepository, DisciplineFileRepository, \
    DisciplineBinaryRepository
from src.repository.grade_repository import GradeRepository, GradeFileRepository, GradeBinaryRepository


class Settings:
    def __init__(self,file_name):
        self._file_name = file_name

    def analyse_settings(self):
        discipline_repo = None
        student_repo = None
        grade_repo = None
        with open(self._file_name ,"r") as file:
            line = file.readline()
            line = line.strip("\n")
            repository,memory_type = line.split("=")
            if memory_type == "binary-file":
                for line in file.readlines():
                    line = line.strip()
                    line = line.strip("\n")
                    repo,name = line.split("=")
                    if name == "disciplines.pickle":
                        discipline_repo = DisciplineBinaryRepository("disciplines.pickle")
                    if name == "students.pickle":
                        student_repo = StudentBinaryRepository("students.pickle")
                    if name == "grades.pickle":
                        grade_repo = GradeBinaryRepository("grades.pickle")
            elif memory_type == "text-file":
                for line in file.readlines():
                    line = line.strip()
                    line = line.strip("\n")
                    repo, name = line.split("=")
                    if name == "disciplines.txt":
                        discipline_repo = DisciplineFileRepository("disciplines.txt")
                    if name == "students.txt":
                        student_repo = StudentFileRepository("students.txt")
                    if name == "grades.txt":
                        grade_repo = GradeFileRepository("grades.txt")
            elif memory_type == "in-memory":
                discipline_repo = DisciplineRepository()
                student_repo = StudentRepository()
                grade_repo = GradeRepository()
        return student_repo,discipline_repo,grade_repo
