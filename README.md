# Smart Directory Organizer

#### Video Demo: <https://youtu.be/OOJmmE7PB-4?si=0_lSrHn9KjEUviue>

### Description

The Smart Directory Organizer is a Python-based tool designed to help you effortlessly organize files within a specified directory by automatically sorting them into user-defined folders based on their file extensions. This project is aimed at improving productivity by maintaining a tidy directory structure, which is particularly useful for managing downloads or workspace directories containing mixed file types.

### Features

- **Automatic Organization**: Files are automatically moved into folders based on their extensions.
- **Customizable**: Users can define their own folder names and extensions mapping.
- **Interactive**: Provides color-coded terminal messages for better user experience.
- **Robustness**: Handles unknown extensions gracefully by skipping those files.

### Explain Functions

1. **main()**: The main function that orchestrates the file organization process.
2. **directory_exist(dir)**: Checks if the specified directory exists. If not, prompts the user to input a valid directory.
3. **get_extensions()**: Prompts the user to input folder names along with their corresponding file extensions.
4. **parse_extensions(lines)**: Converts the user input into a dictionary format that maps file extensions to folder names.
5. **organize_files(directory, reformed_extensions_dict)**: Moves files into their respective folders based on their extensions using the provided directory and mapping.

### Considerations

When developing the Smart directory Organizer, several design choices were made:

1. **User Interaction**: To make the tool user-friendly, I decided to implement a command-line interface with prompts for user inputs. This allows users to specify the directory and extension mappings dynamically.

2. **Error Handling**: Robust error handling was a priority. The script includes checks for directory existence and handles unknown file extensions by skipping those files, which prevents the program from crashing.

3. **Code Modularity**: Functions were designed to be modular and self-contained, making the code easier to read, maintain, and test. For example, the `parse_extensions` function is solely responsible for processing user input into a dictionary format.

4. **Cross-Platform Compatibility**: The tool uses Python's `os` and `shutil` libraries, which are cross-platform, ensuring that the script runs on different operating systems without modification.

### Installation

To use the Smart Directory Organizer, follow these steps:

1. Clone or download the repository:
2. Navigate to the project directory:
3. Install the required packages:

### Usage

1. Run the script.
2. Follow the prompts to select a directory and specify folder names with their corresponding file extensions.
3. The script will organize your files accordingly.

Enjoy a well-organized directory!
