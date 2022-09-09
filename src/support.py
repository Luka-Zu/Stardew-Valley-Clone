from os import walk

def import_folder(path):
    surface_list = []

    for folder in walk(path):
        print("huh")
        print(folder)

    return surface_list