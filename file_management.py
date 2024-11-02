import os

def list_all_files_and_dirs():
    try:
        return os.listdir()
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
            content = file.readlines()
        content.sort()
        with open(file_name, 'w') as file:
            file.writelines(content)
        return f"Content of {file_name} sorted."
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return f"Error sorting file content: {e}"

def list_files_of_extension(extension):
    try:
        return [f for f in os.listdir() if f.endswith(extension)]
    except Exception as e:
        return f"Error listing files of extension '{extension}': {e}"

def sort_files_in_directory(directory="."):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(f)]
        files.sort()
        return files
    except Exception as e:
        return f"Error sorting files in directory '{directory}': {e}"
