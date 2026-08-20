import os
import shutil
def current_directory():
    return os.getcwd()

def show_all_files_and_folders():
    for num ,item in enumerate(os.listdir(),start=1):
        print(num," ",item)

def show_only_file():
    print("Files :")
    for item in os.listdir():
        if os.path.isfile(item):
            print("  " ,item)

def show_only_folder():
    print("Folder :")
    for item in os.listdir():
        if os.path.isdir(item):
            print("  " ,item)


def organize_file():
    photo=0
    txt=0
    python=0
    csv=0
    other=0
    for item in os.listdir():
        if os.path.isfile(item):
            name,extension=os.path.splitext(item)
            folder=""
            if extension.lower() in [".jpg",".png",".jpeg"]:
                folder="photo files"
                photo+=1

            elif extension.lower() == '.txt':
                folder="text files"
                txt+=1

            elif extension.lower() == ".py":
                folder="python files"
                python+=1

            elif extension.lower() == ".csv":
                folder="csv files"
                csv+=1
            else:
                folder="other files"
                other+=1
            if folder:
                if not os.path.exists(folder):
                   os.mkdir(folder)
                path=os.path.join(folder,item)
                shutil.move(item,path)
            
    total=photo+csv+txt+python+other   
    print("=========: Report :==========")
    print("Photo files  :",photo)
    print("CSV files    :",csv)
    print("Text files   :",txt)
    print("Python files :",python)
    print("Other files  :",other)
    print("----------------------------")
    print("Total changes :",total)



while True:
    print("---------- File Organizer and OS and Shutil Use ----------")
    print("1. Current directory")
    print("2. Show all file and folder ")
    print("3. Show file only ")
    print("4. Show folder only ")
    print("5. Orgaize file and report")
    print("6. Exit")
    print("----------------------------------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        location=current_directory()
        print(location)
    elif choice == '2':
        show_all_files_and_folders()

    elif choice == '3':
        show_only_file()

    elif choice == '4':
        show_only_folder()

    elif choice == '5':
        organize_file()

    elif choice == '6':
        print("Program ended .")
        break
    else:
        print("Invalid input .")






            



            


            



