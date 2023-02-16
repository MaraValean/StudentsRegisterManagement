import unittest

from src.domain.grade import Grade
from src.domain.student import Student
from src.exceptions import RepositoryException
from src.repository.discipline_repository import DisciplineRepository
from src.domain.discipline import Discipline
from src.repository.grade_repository import GradeRepository
from src.repository.student_repository import StudentRepository
from src.services.grade_service import GradeService
from src.services.student_service import StudentService
from src.services.discipline_service import DisciplineService

test_repo_students = StudentRepository()
test_repo_disciplines = DisciplineRepository()
test_repo_grades = GradeRepository(test_repo_students, test_repo_disciplines)

test_service_students = StudentService(test_repo_students,test_repo_grades)
test_service_disciplines = DisciplineService(test_repo_disciplines,test_repo_grades)
test_service_grades = GradeService(test_repo_grades,test_repo_students,test_repo_disciplines)


class TestDisciplineRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repository = DisciplineRepository()

    def test_initialize_disciplines__list_updated(self):
        self.__test_repository.initialize_disciplines()
        self.assertEqual(len(self.__test_repository.get_disciplines_list()), 12)

    def test_find_discipline_in_disciplines_list__valid_id__discipline_index(self):
        self.__test_repository.initialize_disciplines()

        self.assertEqual( self.__test_repository.find_discipline_in_disciplines_list("12"),11)

    def test_find_discipline_in_disciplines_list__nonexisting_id__minus_1(self):
        self.__test_repository.initialize_disciplines()

        self.assertEqual( self.__test_repository.find_discipline_in_disciplines_list("20"),-1)
    def test_add_new_discipline__valid_discipline__list_updated(self):

        self.__test_repository.add_new_discipline(Discipline("17","Anatomy"))
        self.assertEqual(len(self.__test_repository.get_disciplines_list()),1)


    def test_add_new_discipline__discipline_id_not_unique__raise_exception(self):

        self.__test_repository.add_new_discipline(Discipline("17","Anatomy"))
        with self.assertRaises(RepositoryException):
            self.__test_repository.add_new_discipline(Discipline("17", "Anatomy"))

    def test_remove_discipline__valid_id__list_updated(self):
        self.__test_repository.initialize_disciplines()
        self.__test_repository.remove_discipline("11")
        self.assertEqual(len(self.__test_repository.get_disciplines_list()), 11)

    def test_remove_discipline__nonexisting_id__raise_exception(self):
        self.__test_repository.initialize_disciplines()
        with self.assertRaises(RepositoryException):
            self.__test_repository.remove_discipline("20")

    def test_update_discipline__valid_id_and_name__list_updated(self):
        self.__test_repository.initialize_disciplines()
        self.__test_repository.update_discipline("12","Chemistry")
        disciplines_list = self.__test_repository.get_disciplines_list()
        discipline = disciplines_list[11]
        self.assertEqual(discipline.name,"Chemistry")

    def test_update_discipline__nonexisting_id__raise_exception(self):
        self.__test_repository.initialize_disciplines()
        with self.assertRaises(RepositoryException):
            self.__test_repository.update_discipline("20","m")

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestStudentRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repository = StudentRepository()

    def test_initialize_students__list_updated(self):
        self.__test_repository.initialize_students()
        self.assertEqual(len(self.__test_repository.get_students_list()), 20)

    def test_find_student_in_students_list__valid_id__student_index(self):
        self.__test_repository.initialize_students()

        self.assertEqual( self.__test_repository.find_student_in_students_list("12"),11)

    def test_find_student_in_students_list__nonexisting_id__minus_1(self):
        self.__test_repository.initialize_students()

        self.assertEqual( self.__test_repository.find_student_in_students_list("30"),-1)
    def test_add_new_student__valid_student__list_updated(self):

        self.__test_repository.add_new_student(Student("27","Ana Tomsa"))
        self.assertEqual(len(self.__test_repository.get_students_list()),1)


    def test_add_new_student__student_id_not_unique__raise_exception(self):

        self.__test_repository.add_new_student(Student("27","Ana tomsa"))
        with self.assertRaises(RepositoryException):
            self.__test_repository.add_new_student(Student("27","Ana tomsa"))
    def test_remove_student__valid_id__list_updated(self):
        self.__test_repository.initialize_students()
        self.__test_repository.remove_student("11")
        self.assertEqual(len(self.__test_repository.get_students_list()), 19)

    def test_remove_student__nonexisting_id__raise_exception(self):
        self.__test_repository.initialize_students()
        with self.assertRaises(RepositoryException):
            self.__test_repository.remove_student("30")

    def test_update_discipline__valid_id_and_name__list_updated(self):
        self.__test_repository.initialize_students()
        self.__test_repository.update_student("12","Maria")
        students_list = self.__test_repository.get_students_list()
        student = students_list[11]
        self.assertEqual(student.name,"Maria")

    def test_update_student__nonexisting_id__raise_exception(self):
        self.__test_repository.initialize_students()
        with self.assertRaises(RepositoryException):
            self.__test_repository.update_student("30","m")

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestGradeRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repository = GradeRepository(StudentRepository(), DisciplineRepository())
        self.__student_repository = StudentRepository()
        self.__discipline_repository = DisciplineRepository()
    """
    def test_add_grade__valid_grade__list_updated(self):
        self.__student_repository.initialize_students()
        self.__discipline_repository.initialize_disciplines()
        self.__test_repository.add_grade(Grade("12","2","9"))
        self.assertEqual(len(self.__test_repository.get_grades_list()),1)
    """


    def test_add_grade__grade_with_nonexisting_student__raise_exception(self):
        self.__student_repository.initialize_students()
        self.__discipline_repository.initialize_disciplines()
        with self.assertRaises(RepositoryException):
            self.__test_repository.add_grade(Grade("32", "2", "9"))

    def test_add_grade__grade_with_nonexisting_discipline__raise_exception(self):
        self.__student_repository.initialize_students()
        self.__discipline_repository.initialize_disciplines()
        with self.assertRaises(RepositoryException):
            self.__test_repository.add_grade(Grade("12", "20", "9"))
    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_grades = GradeRepository(test_repo_students, test_repo_disciplines)
        self.__test_repo_students = StudentRepository()
        self.__test_service_students = StudentService(test_repo_students, test_repo_grades)
        self.__test_repo_disciplines = DisciplineRepository()

    def test_create_students_sorted_by_average_grade__valid_students__list_created(self):
        self.__test_repo_students.add_new_student(Student("10", "Mara"))
        self.__test_repo_students.add_new_student(Student("3", "Maria"))
        self.__test_repo_students.add_new_student(Student("6", "Mama"))
        self.__test_repo_disciplines.initialize_disciplines()
        self.__test_repo_grades.add_grade(Grade("10", "10", "2") )
        self.__test_repo_grades.add_grade(Grade("3", "3", "6") )
        self.__test_repo_grades.add_grade(Grade("6", "6", "4") )
        stud_list = self.__test_service_students.create_students_sorted_by_average_grade()
        self.assertEqual(stud_list[0], "10")
        self.assertEqual(stud_list[1], "3")
        self.assertEqual(stud_list[len(stud_list) - 1], "6")

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestDisciplineService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_grades = GradeRepository(test_repo_students, test_repo_disciplines)
        self.__test_repo_disciplines = DisciplineRepository()
        self.__test_service_disciplines = DisciplineService(test_repo_disciplines, test_repo_grades)

    def test_disciplines_sorted_by_average_grade__valid_grades__list_sorted(self):
        self.__test_repo_grades.add_grade(Grade("10", "10", "2"))
        self.__test_repo_grades.add_grade(Grade("3", "3", "6"))
        self.__test_repo_grades.add_grade(Grade("6", "6", "4"))
        discipline_list = self.__test_service_disciplines.disciplines_sorted_by_average_grade()
        self.assertEqual(discipline_list[0], "3")
        self.assertEqual(discipline_list[1], "6")
        self.assertEqual(discipline_list[len(discipline_list) - 1], "10")

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass


class TestGradeService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo_students = StudentRepository()
        self.__test_repo_disciplines = DisciplineRepository()
        self.__test_repo_grades = GradeRepository(test_repo_students, test_repo_disciplines)
        self.__test_service_grades = GradeService(test_repo_grades, test_repo_students, test_repo_disciplines)

    def test_find_students_failing__2_students_failing__list_created(self):
        self.__test_repo_students.add_new_student(Student("10", "Mara"))
        self.__test_repo_students.add_new_student(Student("3", "Maria"))
        self.__test_repo_students.add_new_student(Student("6", "Mama"))
        self.__test_repo_disciplines.initialize_disciplines()
        self.__test_repo_grades.add_grade(Grade("10", "7", "10"))
        self.__test_repo_grades.add_grade(Grade("3", "8", "2"))
        self.__test_repo_grades.add_grade(Grade("6", "1", "3"))
        grades_list = self.__test_service_grades.find_students_failing()
        self.assertEqual(len(grades_list), 2)

    def test_find_students_failing__no_students_failing__list_empty(self):
        self.__test_repo_students.add_new_student(Student("10", "Mara"))
        self.__test_repo_students.add_new_student(Student("3", "Maria"))
        self.__test_repo_students.add_new_student(Student("6", "Mama"))
        self.__test_repo_disciplines.initialize_disciplines()
        self.__test_repo_grades.add_grade(Grade("10", "7", "10"))
        self.__test_repo_grades.add_grade(Grade("3", "8", "8"))
        self.__test_repo_grades.add_grade(Grade("6", "1", "9"))
        grades_list = self.__test_service_grades.find_students_failing()
        self.assertEqual(len(grades_list), 0)

    def tearDown(self) -> None:
        """
        Runs after all tests are completed
        """
        pass
