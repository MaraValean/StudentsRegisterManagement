from src.domain.discipline import *
from src.domain.student import *
from src.domain.grade import *

from src.repository.discipline_repository import DisciplineRepository, DisciplineFileRepository
from src.repository.student_repository import StudentRepository, StudentFileRepository
from src.repository.grade_repository import GradeRepository, GradeFileRepository

from src.services.discipline_service import DisciplineService
from src.services.student_service import StudentService
from src.services.grade_service import GradeService
from src.services.undo_service import UndoService

from src.ui.ui import Ui

from src.settings import Settings

memory_type = Settings("settings.properties")
student_repo,discipline_repo,grade_repo = memory_type.analyse_settings()

"""
discipline_repo = DisciplineRepository()
student_repo = StudentRepository()
grade_repo = GradeRepository()
"""
service_undo = UndoService()
service_discipline = DisciplineService(discipline_repo,grade_repo,service_undo)
service_student = StudentService(student_repo,grade_repo,service_undo)
service_grade = GradeService(grade_repo,student_repo,discipline_repo,service_undo)

ui = Ui(service_discipline, service_student,service_grade,service_undo)
ui.start()