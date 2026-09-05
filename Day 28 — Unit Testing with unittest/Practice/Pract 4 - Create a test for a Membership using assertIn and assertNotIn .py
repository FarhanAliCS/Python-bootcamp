import unittest
class TestExistness(unittest.TestCase):
    def test_name(self):
        self.assertIn("Afan",n)

    def test_names(self):
        self.assertNotIn("Farhan",n)
        


n=["Ali","Afan","Adnan"]
if __name__ =="__main__":
    unittest.main()
