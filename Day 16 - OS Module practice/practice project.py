import os
def show_crurrent_directry():
    return os.getcwd()


def Show_all_file_and_folder():
    lists=os.listdir()
    for list in lists:
        print(list)


def check_whether_item_exists():
    item=input("Enter file name :")
    if os.path.exists(item):
        print("Item exist .")
    else:
        print("Not exists .")


def create_folder():
    folder=input("Enter folder name to create :")
    if os.path.exists(folder):
        print("Folder already exist .")
    else:
        os.mkdir(folder)


def rename_item():
    item=input("Enter item name :")
    if os.path.exists(item):
        new_name=input("Enter new name :")
        if not os.path.exists(new_name):
           os.rename(item,new_name)
        elif item ==new_name:
            print("Same name not allowed .")
        else:
            print("File already exist .")
    else:
        print("File not exists .")



def delete_item():
    item=input("Enter file name to delete :")
    if os.path.exists(item):
        os.remove(item)
    else:
        print("File not exists .")



def show_file_extension():
    file=input("Enter file name :")
    if os.path.exists(file):
        print(os.path.splitext(file))
    else:
            print("file not exists")



def file_size():
    file=input("Enter file name :")
    if os.path.exists(file):
        print(os.path.getsize(file))
    else:
        print("file not exists")


print("----------------------- File System ----------------------")
while True:
    print("----------------------- File System ----------------------")
    print("1. Show Current directory")
    print("2. show all folder in working file")
    print("3. Check whether item exists")
    print("4. Create new folder")
    print("5. Rename item")
    print("6. Delete file")
    print("7.Show file extention")
    print("8. Show file size")
    print("9. Exit")
    print("---------------------------------------------------------")
    choice=input("Enter your choice :")
    if choice == '1':
        directory=show_crurrent_directry()
        print(directory)

    elif choice == '2':
        Show_all_file_and_folder()

    elif choice == '3':
        check_whether_item_exists()

    elif choice == '4':
        create_folder()

    elif choice == '5':
        rename_item()

    elif choice == '6':
        delete_item()

    elif choice == '7':
        show_file_extension()

    elif choice == '8':
        file_size()

    elif choice == '9':
        print("Program ended .")
        break
    else:
        print("Invalid input .")
        continue


    
    