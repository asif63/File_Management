import os

def list_only_directories(path=None):
    try:
        if path is None:
            path = os.getcwd()  # Default to the current working directory
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    except Exception as e:
        return f"Error listing directories: {e}"


def count_directories(path=None):
    try:
        if path is None:
            path = os.getcwd()  # Default to the current working directory
        return len([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    except Exception as e:
        return f"Error counting directories: {e}"


def count_files(path=None):
    try:
        if path is None:
            path = os.getcwd()  # Default to the current working directory
        return len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    except Exception as e:
        return f"Error counting files: {e}"


# Previous functions remain unchanged

def create_directory(location, dir_name):
    try:
        full_path = os.path.join(location, dir_name)  # Combine the location and the directory name
        os.makedirs(full_path, exist_ok=True)        # Create the directory
        return f"Directory '{dir_name}' created successfully at '{location}'."
    except Exception as e:
        return f"Error creating directory: {e}"


def change_directory(dir_name):
    try:
        os.chdir(dir_name)
        return f"Current directory changed to '{os.getcwd()}'."
    except Exception as e:
        return f"Error changing directory: {e}"

def show_memory_map():
    try:
        result = "\nMemory Map:\n"
        for root, dirs, files in os.walk('.'):
            level = root.replace(os.getcwd(), '').count(os.sep)
            indent = ' ' * 4 * level
            result += f"{indent}{os.path.basename(root)}/\n"
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                result += f"{sub_indent}{f}\n"
        return result
    except Exception as e:
        return f"Error showing memory map: {e}"

