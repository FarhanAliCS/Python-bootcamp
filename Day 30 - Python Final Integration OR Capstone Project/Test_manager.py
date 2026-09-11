import unittest
from unittest.mock import patch
from io import StringIO
from Student import students,Student
from validate_function import(
    marks_to_grade_point,
    validate_name,
    validate_age,
    validate_semester,
    validate_department
)
from Manage import StudentManager 
class TestStudent(unittest.TestCase):
    def test_gpa_calculator(self):
        student=Student(
            "Ali",
            "1234",
            20,
            5,
            "Compputer Science",
            {
                          "Software Engineering" :78.0 ,
                          "Artificial Intelligence": 90.0,
                          "Information Secuity":89.0 ,
                          "Computer Architecture And Organization":78.0,
                          "Probability And Statistics":90.0,
                          "Theory of Atomata":89.0,
                          "Teaching Of Holy Quran":89
            }
        )
        gpa=student.calculate_gpa()
        self.assertAlmostEqual(gpa,3.8)

    def test_empty_subject(self):
        student=Student(
            "Ali",
            "1002",
            23,
            5,
            "Computer Science",
            {}
        )
        self.assertEqual(student.calculate_gpa(),0.0)

############## : Validate Function Test : =================

    def test_grade_point(self):
        self.assertEqual(marks_to_grade_point(85), 4.0)
        self.assertEqual(marks_to_grade_point(80), 3.5)
        self.assertEqual(marks_to_grade_point(75), 3.0)
        self.assertEqual(marks_to_grade_point(50), 1.0)
        self.assertEqual(marks_to_grade_point(40), 0.0)


    def test_validate_name(self):
        validate_name("Ali")
        with self.assertRaises(ValueError):
            validate_name("ab")
        with self.assertRaises(ValueError):
            validate_name("Farhan_")
        with self.assertRaises(ValueError):
            validate_name("Farhan12")
        with self.assertRaises(ValueError):
            validate_name("1234")

    def setUp(self):
        students.clear()
        self.sd=StudentManager()
        students.clear()

    def test_validate_roll_no(self):

        self.sd.validate_roll_no("1564")
        with self.assertRaises(ValueError):
            self.sd.validate_roll_no("100")

        with self.assertRaises(ValueError):
            self.sd.validate_roll_no("abc")

        with self.assertRaises(ValueError):
            self.sd.validate_roll_no("12345")

    def test_validate_age(self):
        validate_age(16)
        with self.assertRaises(ValueError):
            validate_age(15)

        with self.assertRaises(ValueError):
            validate_age(31)


    def test_validate_semester(self):
        validate_semester(6)
        with self.assertRaises(ValueError):
            validate_semester(9)

        with self.assertRaises(ValueError):
            validate_semester(0)

        with self.assertRaises(ValueError):
            validate_semester(-1)

    def test_validate_department(self):
        validate_department("Computer Science")
        with self.assertRaises(ValueError):
            validate_department("Computer_")

        with self.assertRaises(ValueError):
            validate_department("Computer123")

        with self.assertRaises(ValueError):
            validate_department("cs.")

    def test_add_student(self):

        students.clear()

        fake_inputs = [
            "Ali",
            "9999",
            "20",
            "5",
            "Computer Science",
            "80",
            "85",
            "75",
            "70",
            "90",
            "88",
            "82",
            "stop"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.add_student()

            self.assertEqual(len(students), 1)
            self.assertEqual(students[0].name, "Ali")
            self.assertEqual(students[0].roll_no, "9999")
            self.assertEqual(students[0].age, 20)






    def test_search_student(self):

        students.clear()

        students.append(
            Student(
                "Ali",
                "9999",
                20,
                5,
                "Computer Science",
                {
                    "Software Engineering": 80,
                    "Artificial Intelligence": 85,
                    "Information Secuity": 75,
                    "Computer Architecture And Organization": 70,
                    "Probability And Statistics": 90,
                    "Theory of Atomata": 88,
                    "Teaching Of Holy Quran": 82
                }
            )
        )

        fake_inputs = ["9999", "n"]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch("sys.stdout", new_callable=StringIO) as output:

            self.sd.search_student()

        self.assertIn("Ali", output.getvalue())
        self.assertIn("9999", output.getvalue())




   

    def test_delete_student(self):
        students.clear()

        student = Student(
            "Ali",
            "9999",
            20,
            5,
            "Computer Science",
            {
                "Software Engineering": 80.0,
                "Artificial Intelligence": 85.0
            }
        )

        students.append(student)

        fake_inputs = [
            "9999",  # search student
            "y",     # confirm delete
            "n"      # don't delete another
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.delete_student()

        self.assertEqual(len(students), 0)


##### -------------: Student Update Fuction Testing :---------------- ######

    def test_update_student_name(self):
        students.clear()

        student = Student(
            "Ali",
            "9999",
            20,
            5,
            "Computer Science",
            {
                "Software Engineering": 80.0
            }
        )

        students.append(student)

        fake_inputs = [
            "9999",        # roll number
            "Farhan",      # new name
            "y"            # confirm
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_name()

        self.assertEqual(students[0].name, "Farhan")

        students.clear()

    def test_update_student_roll_no(self):
        students.clear()

        student = Student(
            "Ali", "9999", 20, 5, "Computer Science",
            {"Software Engineering": 80.0}
        )
        students.append(student)

        fake_inputs = [
            "9999",
            "8888",
            "y"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_roll_no()

        self.assertEqual(students[0].roll_no, "8888")

        students.clear()


    def test_update_student_age(self):
        students.clear()

        student = Student(
            "Ali", "9999", 20, 5, "Computer Science",
            {"Software Engineering": 80.0}
        )
        students.append(student)

        fake_inputs = [
            "9999",
            "22",
            "y"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_age()

        self.assertEqual(students[0].age, 22)

        students.clear()



    def test_update_student_semester(self):
        students.clear()

        student = Student(
            "Ali", "9999", 20, 5, "Computer Science",
            {"Software Engineering": 80.0}
        )
        students.append(student)

        fake_inputs = [
            "9999",
            "6",
            "y"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_semester()

        self.assertEqual(students[0].semester, 6)

        students.clear()

    def test_update_student_department(self):
        students.clear()

        student = Student(
            "Ali", "9999", 20, 5, "Computer Science",
            {"Software Engineering": 80.0}
        )
        students.append(student)

        fake_inputs = [
            "9999",
            "Artificial Intelligence",
            "y"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_department()

        self.assertEqual(
            students[0].department,
            "Artificial Intelligence"
        )

        students.clear()

    def test_update_student_marks(self):
        students.clear()

        student = Student(
            "Ali", "9999", 20, 5, "Computer Science",
            {
                "Software Engineering": 80.0,
                "Artificial Intelligence": 85.0
            }
        )

        students.append(student)

        fake_inputs = [
            "9999",
            "Software Engineering",
            "95",
            "y"
        ]

        with patch("builtins.input", side_effect=fake_inputs), \
            patch.object(self.sd, "save_to_file"):

            self.sd.update_student_marks()

        self.assertEqual(
            students[0].subjects["Software Engineering"],
            95.0
        )

        students.clear()

###### -------------: Student Statistics :------------- ########

    def test_total_students(self):
        students.clear()

        students.append(
            Student(
                "Ali", "1001", 20, 5, "Computer Science",
                {"Software Engineering": 80.0}
            )
        )

        students.append(
            Student(
                "Farhan", "1002", 21, 5, "Computer Science",
                {"Software Engineering": 90.0}
            )
        )

        result = self.sd.total_students()

        self.assertEqual(result, 2)

        students.clear()

    def test_highest_marks(self):
        students.clear()

        students.append(
            Student(
                "Ali", "1001", 20, 5, "Computer Science",
                {
                    "Software Engineering": 80.0,
                    "Artificial Intelligence": 95.0
                }
            )
        )

        students.append(
            Student(
                "Farhan", "1002", 21, 5, "Computer Science",
                {
                    "Software Engineering": 90.0,
                    "Artificial Intelligence": 85.0
                }
            )
        )

        with patch("sys.stdout", new_callable=StringIO) as output:
            self.sd.highest_marks()

        result = output.getvalue()

        self.assertIn("95", result)
        self.assertIn("Artificial Intelligence", result)

        students.clear()

    def test_lowest_marks(self):
        students.clear()

        students.append(
            Student(
                "Ali", "1001", 20, 5, "Computer Science",
                {
                    "Software Engineering": 80.0,
                    "Artificial Intelligence": 55.0
                }
            )
        )

        students.append(
            Student(
                "Farhan", "1002", 21, 5, "Computer Science",
                {
                    "Software Engineering": 90.0,
                    "Artificial Intelligence": 70.0
                }
            )
        )

        with patch("sys.stdout", new_callable=StringIO) as output:
            self.sd.lowest_marks()

        result = output.getvalue()

        self.assertIn("55", result)
        self.assertIn("Artificial Intelligence", result)

        students.clear()

    def test_average_marks(self):
        students.clear()

        students.append(
            Student(
                "Ali", "1001", 20, 5, "Computer Science",
                {
                    "Software Engineering": 80.0,
                    "Artificial Intelligence": 90.0
                }
            )
        )

        with patch("sys.stdout", new_callable=StringIO) as output:
            self.sd.average_marks()

        result = output.getvalue()

        self.assertIn("85.00", result)

        students.clear()


    def test_student_gpa(self):
        students.clear()

        student = Student(
            "Ali",
            "1001",
            20,
            5,
            "Computer Science",
            {
                "Software Engineering": 80.0,
                "Artificial Intelligence": 90.0
            }
        )

        students.append(student)

        with patch(
            "builtins.input",
            side_effect=["1001", "n"]
        ), patch(
            "sys.stdout",
            new_callable=StringIO
        ) as output:

            self.sd.student_gpa()

        result = output.getvalue()

        self.assertIn("Ali", result)

        students.clear()


    def tearDown(self):
        students.clear()      
        


    
if __name__ == "__main__":
    unittest.main()