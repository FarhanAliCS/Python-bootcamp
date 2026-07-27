#Write in file using 'w'
def write_in_file():
    name=input("Enter your name :")
    with open("name.txt",'w') as file :
     file.write(name)
     print("Data add succesfully")
#Read form file using 'r'
def Read_from_file():
   with open("name.txt",'r') as file:
      print("name :",file.read())
      print("Data read succesfully")


#Write using append 'a'
def add_data_using_append():
   while True:
       name=input("Enter name : or enter 'stop' to exit :" )
       if name.isdigit():
          print("invalid input continue")
          continue
       if name == 'stop':
          break
       with open("name.txt",'a') as file:
        file.write("\n"+name)


#Count of line using 'readlines'
def count_number_of_line():
   count=0
   with open("name.txt",'r') as file:
      data=file.readlines()
      for line in data:
         count+=1
      print("total lines are :",count)


#Read file line by line using 'readline'
def read_line_by_line():
   with open("name.txt",'r') as file:
      data=file.readline()
      for line in range(data):
          print(data[line])
    



#===========================
#      MAIN
#===========================
while True :
        print("========== Task Menu ==========")
        print("1. Write in file 'w' ")
        print("2. Read from file 'r' ")
        print("3. Write in file 'a' append")
        print("4. Count of lines")
        print("5. Read line one by one ")
        print("6. Exit")
        print("===============================")
        choice=input("Enter your choice :")
        if choice == '1':
           write_in_file()
        elif choice == '2':
           Read_from_file()
        elif choice == '3':
           add_data_using_append()
        elif choice == '4':
           count_number_of_line()
        elif choice == '5':
           read_line_by_line()
        elif choice == '6':
           print("program ended .")
           break
        else:
           print("Invalid input .")


