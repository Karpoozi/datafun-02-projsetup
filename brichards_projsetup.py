""" Module 2 Project"""

import pathlib

def create_project_directory(directory_name: str): #param type
    """
    Creates a project sub-directory.
    : param directory_name: Name to be created
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

    def main():
        """ A Project """
        create_project_directory(directory_name='test') # name param
        create_project_directory(directory_name='docs') # name param

        if __name__ == '__main__':
            main()