import os
import shutil

for item in os.listdir():

    if os.path.isfile(item):

        name, extention = os.path.splitext(item)

        folder = ""

        if extention.lower() in [".jpg", ".png"]:
            folder = "jpg or png files"

        elif extention.lower() == ".csv":
            folder = "csv files"

        elif extention.lower() == ".py":
            folder = "python files"

        elif extention.lower() == ".txt":
            folder = "text files"

        if folder:

            if not os.path.exists(folder):
                os.mkdir(folder)

            path = os.path.join(folder, item)

            shutil.move(item, path)
            
                
            


