"""
Project 2 Brooke Richards
This module provides functions for creating a series of project folders. 
"""

# import dependencies
import pathlib
import time
import karpoozi_utils

# create folders for range
def create_folders_for_range(start, end):
    for i in range(start, end+1):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

# create folders from a list
def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    for folder in folder_list:
        if to_lowercase:
            folder = folder.lower()
        if remove_spaces:
            folder = folder.replace(" ", "")
        pathlib.Path(folder).mkdir(exist_ok=True)

# create folders from a list of folder names with prefix 'data'
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

# create a folder every 5 seconds for the duration given
def create_folders_periodically(duration, period):
    start_time = time.time()
    while time.time() - start_time < duration:
        current_time = time.time() - start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period)

# create a path object
project_path = pathlib.Path.cwd()

# define new sub folder path
data_path = project_path.joinpath('data')

# create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def create_project_directory(dir_name: str):
    #creates a project sub-directory
    pathlib.Path(dir_name).mkdir(exist_ok=True)

def main():
    # print byline from imported module
    print(f"Byline: {karpoozi_utils.byline}")

    # create folders for a range 
    create_folders_for_range(start=2020, end=2025)
    
    # create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)
    
    # create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data'
    create_prefixed_folders(folder_names, prefix)
    
    # create folders periodically
    duration_secs = 5
    create_folders_periodically(duration_secs, 1)  # Create a folder every second for 5 seconds

    # test (force lowercase and remove spaces)
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"   
        ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ == "__main__":
    main()
