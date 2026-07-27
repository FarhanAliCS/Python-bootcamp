#add element
def add_element_to_set(marks):
     while True:
          mark=input("Enter marks  or enter 'stop' to exit :")
          if mark=='stop':
               return
          try:
            mark=int(mark)
            marks.add(mark)
          except ValueError:
               print("invald input")
               continue
#remove element
def remove_element(marks):
     for i in marks:
          print(i)
     element=input("Enter element to delete :")
     element=int(element)
     if element in marks:
          marks.discard(element)
     else:
          print("Element not present .")
#check if exist
def Check_if_element_exists(marks):
     if len(marks)==0:
               print("set is empty")
               return
     element=int(input("search if element exists :"))
     
     if element in marks:
          print("element exists")
     else:
        print("element does not exsits .")
#find length
def find_length(marks):
     print("length of marks is :",len(marks))  

#Print set
def show_all_element(marks):
     if len(marks)==0:
          print("set is empty")
          return
     print("marks are :")
     for i in marks:
        print(i)


marks=set()
while True:
          print("============== Main - Menu ==================")
          print("1. add elements")
          print("2. remove elements")
          print("3. searching")
          print("4. length of set")
          print("5. print elements")
          print("6. Exit")
          print("===============================================")
          choice=input("Enter your choice :")

#add element
          if choice == '1':
               add_element_to_set(marks)

#remove element
          elif choice =='2':
               remove_element(marks)

#check if exist
          elif choice == '3':
               Check_if_element_exists(marks)

#find length
          elif choice == '4':
               find_length(marks)

#Print set
          elif choice== '5':
               show_all_element(marks)
          elif choice == '6':
               print("program ended .")
               break
          else:
               print("invalid choice .")