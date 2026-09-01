from pathlib import Path
folder=Path("Practice")

if folder.exists():

    file_name=input("Enter file name :")

    file=folder/file_name

    if file.exists():

        new_name=input("Enter new name :")

        file.rename(folder/new_name)

    else:
        print("File not found .")

else:
    print("Folder not found ..")
