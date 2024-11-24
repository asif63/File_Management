import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, ttk
from file_management import *
from directory_management import *

def display_result(result):
    messagebox.showinfo("Result", result)

def simple_input(prompt):
    return simpledialog.askstring("Input", prompt)

def main_menu(window):
    window.title("Enhanced File Management System")
    window.geometry("800x600")
    window.resizable(True, True)
    
    # ** Set Background Color for the Main Window **
    window.configure(bg='gray35')  # Light blue-gray background
    
    
    
    # Define styles for ttk widgets
    style = ttk.Style()
    style.theme_use('clam')  # 'clam', 'default', 'alt', 'classic'
    
    
    # ** Custom Style for Buttons **
    style.configure(
        'TButton',
        font=('Helvetica', 12),
        padding=10,
        background='papaya whip',    # Button background color
        foreground='gray15',      # Button text color
        focuscolor='none'
    )
    
    title_label = tk.Label(
        window,
        text = "File Management System",
        font = ('Georgia',24,'italic'),
        fg = 'bisque',
        bg = 'gray35'
    )
    title_label.pack(pady = 20)
    
    style.map(
        'TButton',
        background=[('active', '#293241')],  # Darker color when hovered
        foreground=[('active', 'black')]
    )

    # ** Custom Style for Frames **
    style.configure('TFrame', background='gray24')
    
    

    # Create a notebook for tabs
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)
    
    
    
    

    # Sections: File Operations, Directory Operations, Utilities
    tab1 = ttk.Frame(notebook, style='TFrame')
    tab2 = ttk.Frame(notebook, style='TFrame')
    tab3 = ttk.Frame(notebook, style='TFrame')
    
    
    
    notebook.add(tab1, text='File Operations')
    notebook.add(tab2, text='Directory Operations')
    notebook.add(tab3, text='Utilities')
    
    

    # Function to add buttons in grid layout
    def add_buttons(tab, button_texts, commands):
        for i, (text, cmd) in enumerate(zip(button_texts, commands)):
            row, col = divmod(i, 2)  # 2 buttons per row
            button = ttk.Button(tab, text=text, command=cmd, style='TButton')
            button.grid(row=row, column=col, padx=20, pady=10, sticky='ew')

    # File Operations
    file_ops_texts = [
        "List all files and directories", "Create new file",
        "Delete file", "Rename file",
        "Edit file content", "Read from a file",
        "Move a file"
    ]
    file_ops_commands = [
        lambda: display_result(list_all_files_and_dirs(filedialog.askdirectory())),
        lambda: display_result(create_file(filedialog.asksaveasfilename())),
        lambda: display_result(delete_file(filedialog.askopenfilename())),
        lambda: display_result(rename_file(filedialog.askopenfilename(), filedialog.asksaveasfilename())),
        lambda: display_result(edit_file_content(filedialog.askopenfilename(), simple_input("Enter new content:"))),
        lambda: display_result(read_file(filedialog.askopenfilename())),
        lambda: display_result(move_file(filedialog.askopenfilename(), filedialog.askdirectory())),
    ]
    add_buttons(tab1, file_ops_texts, file_ops_commands)

    # Directory Operations
    dir_ops_texts = [
        "Create Directory", "Create a file in a directory",
        "List only directories", "List files of specific extension",
        "Count directories", "Count files",
        "Sort files in directory"
    ]
    dir_ops_commands = [
        lambda: display_result(create_directory(filedialog.askdirectory(), simple_input("Enter directory name:"))),
        lambda: display_result(create_file_in_directory(filedialog.askdirectory(), simple_input("Enter file name:"))),
        lambda: display_result(list_only_directories(filedialog.askdirectory())),
        lambda: display_result(list_files_of_extension(simple_input("Enter extension (e.g., .txt):"), filedialog.askdirectory())),
        lambda: display_result(count_directories(filedialog.askdirectory())),
        lambda: display_result(count_files(filedialog.askdirectory())),
        lambda: display_result(sort_files_in_directory(filedialog.askdirectory()))
    ]
    add_buttons(tab2, dir_ops_texts, dir_ops_commands)

    # Utility Functions
    util_texts = [
        "Search files", "Sort file content",
        "Get file details", "Show memory map",
        "Change current directory"
    ]
    util_commands = [
        lambda: display_result(search_file(simple_input("Enter search query:"))),
        lambda: display_result(sort_file_content(filedialog.askopenfilename())),
        lambda: display_result(file_details(filedialog.askopenfilename())),
        lambda: display_result(show_memory_map()),
        lambda: display_result(change_directory(filedialog.askdirectory()))
    ]
    add_buttons(tab3, util_texts, util_commands)

    # Make columns expand equally
    for tab in [tab1, tab2, tab3]:
        for i in range(2):  # 2 columns
            tab.columnconfigure(i, weight=1)

    window.mainloop()

# Initialize the GUI
if __name__ == "__main__":
    root = tk.Tk()
    main_menu(root)
