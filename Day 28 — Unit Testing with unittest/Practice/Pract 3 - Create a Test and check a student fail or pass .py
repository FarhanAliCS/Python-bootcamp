import unittest
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    marks: int

    def is_passed(self) -> bool:
        return self.marks >=50

class TestStudent(unittest.TestCase):
    def test_ispassed(self):
        self.assertTrue(student.is_passed())
    def test_isFail(self):
        self.assertFalse(student2.is_passed())

student=Student("farhan",78)
student2=Student("Ali",45)

if __name__ == "__main__":
    unittest.main()

