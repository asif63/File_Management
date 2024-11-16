import os

def list_only_directories():
    try:
        return [d for d in os.listdir() if os.path.isdir(d)]
    except Exception as e:
        return f"Error listing directories: {e}"

def count_directories():
    try:
        return len(list_only_directories())
    except Exception as e:
        return f"Error counting directories: {e}"

def count_files():
    try:
        return len([f for f in os.listdir() if os.path.isfile(f)])
    except Exception as e:
        return f"Error counting files: {e}"

# Previous functions remain unchanged

def create_directory(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        return f"Directory '{dir_name}' created successfully."
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

