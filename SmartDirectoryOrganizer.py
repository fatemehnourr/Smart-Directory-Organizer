""" << Smart Directory Organizer >>
    Fatemeh Nourian Ramsheh
    @fatemehnourr (GitHub and edX username)
    Tehran, Iran
    6 August 2024 """

import os
import shutil
from colorama import init, Fore

# Initialize colorama for colored text in the console
init(autoreset=True)

def main():
    print("======= Smart File Organizer =======")
    dir = input("Select a directory to organize: ")
    isdir , dir = directory_exist(dir)
    # Check if the provided directory exists
    if isdir:
        directory = dir
    
    # Get file extensions and corresponding folder names from user
    lines = get_extensions()
    
    # Parse the extensions input into a usable dictionary format
    reformed_extensions_dict = parse_extensions(lines)
    
    # Organize the files in the provided directory based on the parsed dictionary
    organize_files(directory, reformed_extensions_dict)
    print("======= File organization completed! =======")


def directory_exist(dir):
    while True:
        if os.path.isdir(dir):
            break
        else:
            print(Fore.RED +"This directory Does NOT exist! Please try again.")
            dir = input("Select a directory to organize: ")
    return True,dir


def get_extensions():
    lines = []
    print("Alright! Now type folders name with extension:"
          "\n(for example =\nImages : .jpg , .png\nVideos : .mkv , .mp4 , .webm)"
          "\nAt the end type \"END\" in a new line and press ENTER!")

    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)

    return lines


def parse_extensions(lines):
    extensions_dict = {}
    reformed_extensions_dict = {}

    for line in lines:
        folder_name, extensions = line.split(":")
        folder_name = folder_name.strip()
        extensions_list = extensions.split(",")
        stripped_extensions_list = [ext.strip() for ext in extensions_list]
        extensions_dict[folder_name] = stripped_extensions_list

    for folder, extensions in extensions_dict.items():
        for ext in extensions:
            reformed_extensions_dict[ext] = folder
        
    return reformed_extensions_dict


def organize_files(directory, reformed_extensions_dict):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension in reformed_extensions_dict:
                folder_name = reformed_extensions_dict[file_extension]
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, file_name)
                shutil.move(file_path, destination_path)

                print(Fore.GREEN + f"Moved {file_name} to {folder_name} folder.")
            else:
                print(Fore.RED + f"Skipped {file_name}. Unknown file extension.")
        else:
            print(Fore.YELLOW + f"Skipped {file_name}. It is a directory.")


if __name__ == "__main__":
    main()
