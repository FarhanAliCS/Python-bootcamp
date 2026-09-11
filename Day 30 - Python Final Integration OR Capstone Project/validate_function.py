import logging
# ==================== Logging Setup ====================

file = logging.FileHandler("Student.log")
terminal = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file.setFormatter(formatter)
terminal.setFormatter(formatter)

file.setLevel(logging.DEBUG)
terminal.setLevel(logging.INFO)

logging.basicConfig(
    handlers=[file, terminal],
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# ==================== Validation Functions ====================

def validate_name(name: str) -> None:
    if not name.replace(" ", "").isalpha():
        logger.debug("Invalid student name.")
        raise ValueError(
            "Only alphabets are allowed in student name."
        )

    if len(name) < 3:
        logger.debug("Student name must contain at least 3 characters.")
        raise ValueError(
            "Student name must be 3 or more characters."
        )


def validate_age(age: int) -> None:
    if not 16 <= age <= 25:
        logger.debug(f"{age} is not a valid age.")
        raise ValueError(
            "Age must be between 16 - 25."
        )



def validate_marks(marks: float) -> None:
    if not 0 <= marks <= 100:
        logger.debug(f"{marks} is not valid marks.")
        raise ValueError(
            "Marks must be between 0 - 100."
        )


def validate_semester(semester: int) -> None:
    if not 1 <= semester <= 8:
        logger.debug(f"{semester} is not a valid semester.")
        raise ValueError(
            "Semester must be between 1 - 8."
        )


def validate_department(department: str) -> None:
    if not department.replace(" ", "").isalpha():
        logger.debug(f"{department} is not a valid department.")
        raise ValueError(
            "Only alphabets are allowed in department name."
        )


# ==================== Student Display ====================

def display_student_info(student) -> None:
    print(f"Name             : {student.name}")
    print(f"Roll No          : {student.roll_no}")
    print(f"Age              : {student.age}")
    print(f"Semester         : {student.semester}")
    print(f"Department       : {student.department}")

    print("\n---------- Student Marks ----------")

    for subject, marks in student.subjects.items():
        print(f"{subject:<40}: {marks}")


# ==================== Marks → Grade Point ====================

def marks_to_grade_point(marks: float) -> float:

    if marks >= 85:
        return 4.0
    elif marks >= 84:
        return 3.9
    elif marks >= 83:
        return 3.8
    elif marks >= 82:
        return 3.7
    elif marks >= 81:
        return 3.6
    elif marks >= 80:
        return 3.5
    elif marks >= 79:
        return 3.4
    elif marks >= 78:
        return 3.3
    elif marks >= 77:
        return 3.2
    elif marks >= 76:
        return 3.1
    elif marks >= 75:
        return 3.0
    elif marks >= 74:
        return 2.9
    elif marks >= 73:
        return 2.8
    elif marks >= 72:
        return 2.7
    elif marks >= 71:
        return 2.6
    elif marks >= 70:
        return 2.5
    elif marks >= 69:
        return 2.4
    elif marks >= 68:
        return 2.3
    elif marks >= 67:
        return 2.2
    elif marks >= 66:
        return 2.1
    elif marks >= 65:
        return 2.0
    elif marks >= 64:
        return 1.9
    elif marks >= 63:
        return 1.8
    elif marks >= 62:
        return 1.7
    elif marks >= 61:
        return 1.6
    elif marks >= 50:
        return 1.0
    else:
        return 0.0