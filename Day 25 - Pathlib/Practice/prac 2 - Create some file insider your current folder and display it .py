from pathlib import Path
folder=Path("Day 25 - Pathlib") /"Practice"

if not folder.exists():
    folder.mkdir(parents=True)
for name in ["data.txt","photo.jpg","file.py","info.csv"]:
        file=folder/name
        file.touch(exist_ok=True)
print("Files Created succesfully .")

#Print all files 
try:
 for files in folder.iterdir():
      if files.is_file():
         print(files," File")
      elif files.is_dir():
           print(files," Folder")
except ValueError :
    print("File not found .")

    
