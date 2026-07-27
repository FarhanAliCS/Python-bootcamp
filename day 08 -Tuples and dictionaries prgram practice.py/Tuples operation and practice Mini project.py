#Printing all marks 
from itertools import count


def print_marks(marks):
    print("marks :",marks)

#Find length of tuple
def find_length(marks):
    print("length :",len(marks))


#Count of all element
def count_elements(marks):
    print("count :",len(marks))



#Find Indix of element of marks tuple
def find_indix_of_element(marks):
 print_marks(marks)
 while True:
     try:
        element=input("Enter element or enter 'stop' to exit  :")
     except ValueError:
         print("invalid input ")
         continue
     
     if element=='stop':
         break
     element=int(element)
    
     if element not in marks:
         print("element does not exist .")
         continue
     if element in marks:
         print("Index is :",marks.index(element))
        
        

#================================#
#      Main Menu                 #
#================================#

marks=(90,32,43,54,65,76,54)
while True:
      print("=========== Task Menu =============")
      print("1. print all marks ")
      print("2. Find length of tuple")
      print("3. Count all element in tuple")
      print("4. Find element indix ")
      print("5. Exit ")
      print("===================================")
      choice=input("Enter you choice :")
      if choice == '1':
          print_marks(marks)
      elif choice == '2':
          find_length(marks)
      elif choice == '3':
          count_elements(marks)
      elif choice == '4':
          find_indix_of_element(marks)
      elif choice =='5':
          print("prgram ended")
          break
      else:
          print("invalid choice")