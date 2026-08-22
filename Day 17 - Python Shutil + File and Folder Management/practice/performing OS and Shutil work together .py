import os
import shutil
file=input("Enter file name :")

if os.path.exists(file):

   if not os.path.exists("Backup"):

      os.mkdir("Backup")

   path=os.path.join("Backup","data.txt")

   shutil.copy(file,path)

else:

  print("File does not exists .")
