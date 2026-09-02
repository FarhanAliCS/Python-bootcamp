import logging

#User login logger
logging.basicConfig(filename="login.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

def login(name,password):
     logging.info("Login starts ")
     user_name=input("Enter user_name :")
     user_password=input("Enter user password :")

     if user_name == name and user_password == password :
          logging.info("Login succesfully .")
          print("You login succesfully .")
     
     else:
          logging.warning("Invalid user_name or password .")
          print("invalid user_name or password . try again !")
          logging.error("Login error occur .")

login("Farhan","far1234")

     

            

