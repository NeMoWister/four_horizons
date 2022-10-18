import os

filename = "bg_list.txt"
with open(filename, "w", encoding="utf-8") as bg_list:
    for f_name in os.listdir(os.getcwd()):
        name, ext = os.path.splitext(f_name)
        if ext in {".jpg", ".png"}:
            bg_list.write('image bg ' + name + ' = "bgs/' + f_name +'"\n')
