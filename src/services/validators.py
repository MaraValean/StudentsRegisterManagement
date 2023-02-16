from src.exceptions import ValidatorException


class DisciplineValidator:
    @staticmethod
    def validate_discipline(discipline):
        errors=""
        if discipline.id.isnumeric()==False:
            errors += "Discipline id must be an integer\n"
        if discipline.name.isalpha()==False:
            errors += "Discipline name must be a string\n"
        if len(errors):
            raise ValidatorException(errors)


class StudentValidator:
    @staticmethod
    def validate_student(student):
        errors=""
        if student.id.isnumeric()==False:
            errors += "Student id must be an integer\n"
        #if student.name.strip().isalpha()==False:
           # errors += "Student name must be a string\n"
        if len(errors):
            raise ValidatorException(errors)


class GradeValidator:
    @staticmethod
    def validate_grade(grade):
        errors = ""
        if grade.discipline_id.isnumeric() == False:
            errors += "Discipline id must be an integer\n"
        if grade.student_id.isnumeric() == False:
            errors += "Student id must be an integer\n"
        if grade.grade_value.isnumeric() == False:
            errors += "Grade value must be an integer\n"
        if grade.grade_value.isnumeric() == True and int(grade.grade_value) not in range (0,11):
            errors += "Grade value must be between 0 and 10\n"
        if len(errors):
            raise ValidatorException(errors)
