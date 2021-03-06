import os
import pickle as pkl


class FileWriter:

    def __init__(self, path):
        """path - путь до файла"""
        self.path_ = path
        self.file = None

    def __enter__(self):
        self.file = open(self.path, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()

    path = property()

    @path.getter
    def path(self):
        return self.path_

    @path.setter
    def path(self, new_path):
        self.__init__(new_path)

    @path.deleter
    def path(self):
        self.path_ = ''


    def print_file(self):
        with open(self.path) as file:
            if file is None:
                print('No such file')
            else:
                file_content = file.read()
                print(file_content)
                file.close()

    def write(self, some_string):
        self.file.write(some_string)

    def save_yourself(self, file_name):
        self.file = None
        with open(file_name, 'wb') as file:
            pkl.dump(self, file)


    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as file:
            new_object = pkl.load(file)
        return new_object