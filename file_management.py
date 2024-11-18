import os

def list_all_files_and_dirs(path=None):
    try:
        if path is None:
            path = os.getcwd()  # Default to the current working directory if no path is provided
        return os.listdir(path)
    except Exception as e:
        return f"Error listing files and directories: {e}"


def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            pass
        return f"{file_name} created."
    except Exception as e:
        return f"Error creating file: {e}"

def delete_file(file_name):
    try:
        os.remove(file_name)
        return f"{file_name} deleted."
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return f"Error deleting file: {e}"

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return f"{old_name} renamed to {new_name}."
    except FileNotFoundError:
        return f"File {old_name} not found."
    except Exception as e:
        return f"Error renaming file: {e}"

def edit_file_content(file_name, new_content):
    try:
        with open(file_name, 'w') as file:
            file.write(new_content)
        return f"Content written to {file_name}."
    except Exception as e:
        return f"Error editing file content: {e}"

def search_file(query):
    try:
        files = [f for f in os.listdir() if query in f]
        return files if files else f"No files found with query '{query}'."
    except Exception as e:
        return f"Error searching files: {e}"

def file_details(file_name):
    try:
        file_info = os.stat(file_name)
        return {
            "size": file_info.st_size,
            "created": file_info.st_ctime,
            "modified": file_info.st_mtime,
        }
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return f"Error getting file details: {e}"

def sort_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        # Split content into words, sort them, and join them back
        sorted_content = ' '.join(sorted(content.split()))
        
        # Write the sorted content back to the file
        with open(file_name, 'w') as file:
            file.write(sorted_content)
        
        return f"Content of {file_name} sorted alphabetically by words."
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return f"Error sorting file content: {e}"


def list_files_of_extension(extension, path=None):
    try:
        if path is None:
            path = os.getcwd()  # Default to the current working directory
        return [f for f in os.listdir(path) if f.endswith(extension) and os.path.isfile(os.path.join(path, f))]
    except Exception as e:
        return f"Error listing files of extension '{extension}': {e}"


def sort_files_in_directory(directory="."):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(f)]
        files.sort()
        return files
    except Exception as e:
        return f"Error sorting files in directory '{directory}': {e}"
import os
import shutil

# Previous functions remain unchanged

def create_file_in_directory(directory, file_name):
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write("")
        return f"File '{file_name}' created in directory '{directory}'."
    except Exception as e:
        return f"Error creating file in directory: {e}"

def move_file(src, dest):
    try:
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(src, dest)
        return f"File '{src}' moved to '{dest}'."
    except Exception as e:
        return f"Error moving file: {e}"

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return f"Content of '{file_name}':\n{content}"
    except Exception as e:
        return f"Error reading file: {e}"

