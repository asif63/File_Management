def display_main_menu():
    print("\nFile Management System")
    print("1. List all files and directories")
    print("2. Create new file")
    print("3. Delete file")
    print("4. Rename file")
    print("5. Edit file content")
    print("6. Search files")
    print("7. Get file details")
    print("8. Sort file content")
    print("9. List only directories")
    print("10. List files of specific extension")
    print("11. Count directories")
    print("12. Count files")
    print("13. Sort files in directory")
    print("14. Create a directory")
    print("15. Create a file in a directory")
    print("16. Change current directory")
    print("17. Move a file")
    print("18. Read from a file")
    print("19. Show memory map")
    print("0. Exit")

def get_user_input():
    return input("Choose an option: ")

def display_results(result):
    print(result)
