from dataclasses import dataclass

from validate_function import marks_to_grade_point

@dataclass
class Student:
    name: str
    roll_no: str
    age: int
    semester: int
    department: str
    subjects: dict[str, float]

    def calculate_gpa(self) -> float:
        if not self.subjects:
            return 0.0

        grade_points = [
            marks_to_grade_point(marks)
            for marks in self.subjects.values()
        ]

        return sum(grade_points) / len(grade_points)


students: list[Student] = []

