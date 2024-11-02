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
