import unittest
class TestDivision(unittest.TestCase):
    def test_result(self):
        self.assertEqual(divide(10,2),5)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)


def divide(a,b):
    if b==0:
        raise ZeroDivisionError
    return a/b

if __name__ == "__main__":
    unittest.main()

