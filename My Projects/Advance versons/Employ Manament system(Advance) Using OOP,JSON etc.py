import json
#Class
class Employes:
    # Constructor
    def __init__(self):
        self.data="employ_data.json"
        try:
            with open(self.data ,'r') as file:
             self.employe=json.load(file)
        except ( FileNotFoundError, json.JSONDecodeError):
           self.employe={}


# Save data to json file
    def save_to_file(self):
       with open(self.data,'w') as file:
          json.dump(self.employe,file,indent= 4)



# Add new employee
    def add_employ(self):
             while True:
                 try:
                     id=input("Enter employe ID : or enter (stop) to exit :")
                     if id.lower()== "stop":
                         break
                     if id =='0000':
                         raise ValueError("0000 not allowed in id .")
                     if id in self.employe:
                         raise ValueError(" Id already exist try another one .")
                     if id.replace(" "," ").isalpha():
                          raise ValueError("Id must be an integer .")
                     if len(id) != 4:
                         raise ValueError("Length of id must be four")
                     
                 except ValueError as e :
                     print("Error :",e)
                     continue
                 while True:
                     try:
                         name=input("Enter employee name :").strip().title()
                         if not name.replace(" ","").isalpha():
                             raise ValueError ("Numbers are special characters not alowed in name .")
                         else:
                             break
                     except ValueError as e:
                         print("Error :",e)
                         continue
                 while True:
                     try:
                         salary=int(input("Enter employee salary :"))
                         if 15000 <= salary <=100000:
                             break
                         else:
                             raise ValueError ("Salary must be atlest 15000 and anword .")
                     except ValueError as e:
                         print("Error :",e)
                         continue
                 while True:
                     try:
                         department_n=["sales","HR","Marketing",":development"]
                         department=input("Enter your department :")
                         if not department.replace(" ","").isalpha():
                             raise ValueError ("Integer and special charcter not allowed in department name .")
                         if department in department_n:
                             break
                         else:
                             raise ValueError ("Department must be of in department",department_n)
                     except ValueError as e:
                         print("Error :",e)
                 self.employe[id]={
                     "Name" : name,
                     "Salary" : salary,
                     "Department" : department
                 }
                 self.save_to_file()
                 print("Employee add succesfully .")
    

# Print all employes
    def show_data(self):
       if not self.employe:
          print("Empty dictionary .")
          return
       count=0
       for id, details in self.employe.items():
          count+=1
          print(f"===== Employe {count} ====== ")
          print(f"ID         :     {id}")
          print(f"Name       :      {details["Name"]}")
          print(f"Salary     :      {details["Salary"]}")
          print(f"Depatment  :      {details["Department"]}")



#Showing detils in some places like searching and updating emloyee
    def display(self,id,details):
            print(f"===== Employe ====== ")
            print(f"ID         :     {id}")
            print(f"Name       :      {details["Name"]}")
            print(f"Salary     :      {details["Salary"]}")
            print(f"Depatment  :      {details["Department"]}")


#Search Employee by id
    def search_employee(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        while True:
            try: 
               search=input("Enter employe ID :")
               if search.replace(" "," ").isalpha():
                   raise ValueError("Id must be an integer .")
                                     
            except ValueError as e :
               print("Error :",e)
               continue
            else:
                if search not in self.employe:
                   print("Not found .")
                   break
                details=self.employe[search]
                self.display(search,details)
                break


#Delete employee
    def delete_employee(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        while True:
            try:
                delete=input("Enter  Id to delete Employee:")
                if delete.replace(" "," ").strip and delete.isalpha():
                   raise ValueError("Id must be an integer .")
                if len(delete) != 4:
                  raise ValueError("Length of id must be four")
            except ValueError as e:
                print("Error :",e)
                continue
            else:
                if delete in self.employe:
                    if delete not in self.employe:
                        print("No maching employee for id",delete)
                        break
                    del self.employe[delete]
                    self.save_to_file()
                    print("Delete succesfully .")
                    break


#Search by name
    def search_by_name(self):
        if not self.employe:
           print("Empty dictionary .")
           return
        while True:
           try:
             name=input("Enter empoyee name to search :").strip().title()
             if not name.replace(" ","").isalpha():
                 raise ValueError ("Integer and special character not accepted in name .")
           except ValueError as e:
               print("Error :",e)
               continue
               
           else: 
             found=False
             for id, details in self.employe.items():
               if details["Name"]==name:
                   self.display(id,details)
                   found=True
                   break
             if not found:
                   print("No employee on name ",name)
             break
               
#Update Name
    def update_name(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        while True:
         try:
            update=input("Input Employee id to update name :")
            if update.replace(" "," ").isalpha():
               raise ValueError("Id must be an integer .")
         except ValueError as e:
             print("Error :",e)
             continue
         found=False
         for key ,details in self.employe.items():
             if key==update:
                 while True:
                     try:
                         new_name=input("Enter emloyee name to update:")
                         if not new_name.replace(" ","").isalpha():
                             raise ValueError("Integer or special character not allowed in name .")
                     except ValueError as e:
                         print("Error :",e)
                         continue
                     details["Name"]=new_name
                     self.save_to_file()
                     print("Name update succesfully .")
                     found=True
                     break
         if not found:
             print("Not found .")
         break

#Update salary
    def update_salary(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        while True:
         try:
            update=input("Input Employee id  :")
            if update.replace(" "," ").isalpha():
               raise ValueError("Id must be an integer .")
         except ValueError as e:
             print("Error :",e)
             continue
         found=False
         for key ,details in self.employe.items():
             if key==update:
                 while True:
                     try:
                         salary=input("Enter emloyee name to update:")
                         if not 15000 <= salary <=100000:
                            raise ValueError ("Salary must be atlest 15000 and anword .")
                     except ValueError as e:
                         print("Error :",e)
                         continue
                     
                     details["Salary"]=salary
                     self.save_to_file()
                     print("Name update succesfully .")
                     found=True
                     break
         if not found:
             print("Not found .")
         break

#Update department
    def update_department(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        while True:
         try:
            update=input("Enter Employee id  :")
            if update.replace(" "," ").isalpha():
               raise ValueError("Id must be an integer .")
         except ValueError as e:
             print("Error :",e)
             continue
         found=False
         for key ,details in self.employe.items():
             if key==update:
                 while True:
                     try:
                         department_n=["sales","HR","Marketing","Develpment"]
                         new_department=input("Enter emloyee name to update:")
                         if not new_department.replace(" ","").isalpha():
                             raise ValueError("Integer or special character not allowed in name .")
                         if new_department not in department_n:
                             raise ValueError ("Department must be of in department",department_n)
                     except ValueError as e:
                         print("Error :",e)
                         continue
                     details["Department"]=new_department
                     self.save_to_file()
                     print("Name update succesfully .")
                     found=True
                     break
         if not found:
             print("Not found .")
         break


#Total employees
    def total_employee(self):
        if not self.employe:
            print("Empty dictionary .")
            return
        count=0
        for id in self.employe.keys():
            count+=1
        return count
             
            
        
        
        
#================#
#      MAIN      #
#================#
employes_info=Employes()
while True:
    print(": ========= Employee Managment System ========== :")
    print("1. Add Employee")
    print("2. Search Employee by ID .")
    print("3. Search Employee by name ")
    print("4. Delete Emloyee ")
    print("5. Update Name")
    print("6. Update Salary")
    print("7. Update Department ")
    print("8. Show all Employess ")
    print("9. Number of Emloyees")
    print("10. Exit")
    print("===============================================")
    choice=input("Enter your choice :")
    if choice == '1':
        employes_info.add_employ()
    elif choice == '2':
        employes_info.search_employee()
    elif choice == '3':
        employes_info.search_by_name()
    elif choice == '4':
        employes_info.delete_employee()
    elif choice == '5':
        employes_info.update_name()
    elif choice == '6':
        employes_info.update_salary()
    elif choice == '7':
        employes_info.update_department()
    elif choice == '8':
        employes_info.show_data()
    elif choice == '9':
        print(employes_info.total_employee())
       

             
                
                

             

        
          

