import tkinter as tk
from tkinter import messagebox, filedialog
from file_management import *
from directory_management import *

def display_result(result):
    messagebox.showinfo("Result", result)

def main_menu(window):
    window.title("File Management System")
    window.geometry("600x400")

    options = [
        "List all files and directories",
        "Create new file",
        "Delete file",
        "Rename file",
        "Edit file content",
        "Search files",
        "Get file details",
        "Sort file content",
        "List only directories",
        "List files of specific extension",
        "Count directories",
        "Count files",
        "Sort files in directory",
        "Create a directory",
        "Create a file in a directory",
        "Change current directory",
        "Move a file",
        "Read from a file",
        "Show memory map"
    ]

    def execute_choice(choice):
        if choice == 1:
           folder_path = filedialog.askdirectory(title="Select a Directory or Drive")
           if folder_path:
            display_result(list_all_files_and_dirs(folder_path))
           else:
            display_result("No directory selected.")
        elif choice == 2:
            file_name = filedialog.asksaveasfilename()
            if file_name:
                display_result(create_file(file_name))
        elif choice == 3:
            file_name = filedialog.askopenfilename()
            if file_name:
                display_result(delete_file(file_name))
        elif choice == 4:
            old_name = filedialog.askopenfilename()
            new_name = filedialog.asksaveasfilename()
            if old_name and new_name:
                display_result(rename_file(old_name, new_name))
        elif choice == 5:
            file_name = filedialog.askopenfilename()
            if file_name:
                new_content = simple_input("Enter new content:")
                display_result(edit_file_content(file_name, new_content))
        elif choice == 6:
            query = simple_input("Enter search query:")
            if query:
                display_result(search_file(query))
        elif choice == 7:
            file_name = filedialog.askopenfilename()
            if file_name:
                display_result(file_details(file_name))
        elif choice == 8:
            file_name = filedialog.askopenfilename()
            if file_name:
                display_result(sort_file_content(file_name))
        elif choice == 9:  # List only directories
         directory_path = filedialog.askdirectory(title="Select a Directory")
         if directory_path:
          display_result(list_only_directories(directory_path))
         else:
           display_result("No directory selected.")

        elif choice == 10:  # List files of a specific extension
         directory_path = filedialog.askdirectory(title="Select a Directory")
         if directory_path:
           extension = simple_input("Enter file extension (e.g., .txt):")
           if extension:
            display_result(list_files_of_extension(extension, directory_path))
           else:
            display_result("No extension entered.")
         else:
            display_result("No directory selected.")

        elif choice == 11:  # Count directories
         directory_path = filedialog.askdirectory(title="Select a Directory")
         if directory_path:
          display_result(count_directories(directory_path))
         else:
          display_result("No directory selected.")

        elif choice == 12:  # Count files
          countfiles = filedialog.askdirectory(title="Select a Directory")
          if countfiles:
           display_result(count_files(countfiles))
          else:
            display_result("No directory selected.")

        elif choice == 13:
            directory = filedialog.askdirectory()
            if directory:
                display_result(sort_files_in_directory(directory))
        elif choice == 14:  # Create directory
            location = filedialog.askdirectory()
            dir_name = simple_input("Enter the directory name:")
            display_result(create_directory(location, dir_name))

        elif choice == 15:
            dir_name = filedialog.askdirectory()
            if dir_name:
                file_name = simple_input("Enter file name:")
                if file_name:
                    display_result(create_file_in_directory(dir_name, file_name))
        elif choice == 16:
            dir_name = filedialog.askdirectory()
            if dir_name:
                display_result(change_directory(dir_name))
        elif choice == 17:
            src = filedialog.askopenfilename()
            dest = filedialog.askdirectory()
            if src and dest:
                display_result(move_file(src, dest))
        elif choice == 18:
            file_name = filedialog.askopenfilename()
            if file_name:
                display_result(read_file(file_name))
        elif choice == 19:
            display_result(show_memory_map())

    for idx, option in enumerate(options, start=1):
        tk.Button(window, text=option, command=lambda c=idx: execute_choice(c)).pack(fill="x", pady=5)

def simple_input(prompt):
    input_window = tk.Toplevel()
    input_window.title(prompt)

    tk.Label(input_window, text=prompt).pack(pady=10)
    entry = tk.Entry(input_window, width=40)
    entry.pack(pady=10)

    input_value = tk.StringVar()  # Variable to store the input value

    def on_submit():
        input_value.set(entry.get())  # Store the entry value in the variable
        input_window.destroy()  # Close the input window

    tk.Button(input_window, text="Submit", command=on_submit).pack(pady=10)
    input_window.wait_window()  # Wait for the input window to close

    return input_value.get()  # Return the stored input value

