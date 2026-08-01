def file_opening_safely(demo):
 try:
  with open(demo,'r') as file:
   data=file.read()

 except FileNotFoundError:
  print("file not found")

 except PermissionError:
  print("acces denied")

 except Exception as e:
  print("error is ",e)

 else:
  print(data)

 finally:
  print("Program end .")

demo="dem.txt"   
file_opening_safely(demo)
