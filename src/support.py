import os
from os import walk


def import_folder(path):
    surface_list = []

    for fl in os.walk(path, topdown=True):
        print(fl)

    return surface_list
