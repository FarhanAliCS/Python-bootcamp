import unittest
import main

class UserValidationCheck(unittest.TestCase):
     
     def test_username(self):
          self.assertTrue(main.validate_username("Farhan"))
          self.assertFalse(main.validate_username("Ali"))


     def test_userage(self):
          self.assertTrue(main.validate_age(18))
          self.assertTrue(main.validate_age(24))
          self.assertFalse(main.validate_age(17))

     def test_createUser(self):
          self.assertTrue(main.create_user("Farhan",18))
          with self.assertRaises(ValueError):
               main.create_user("Ali",14)
          
          

if __name__ == "__main__":
    unittest.main()
