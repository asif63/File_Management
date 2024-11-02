from file_management import *
from directory_management import *
from interface import display_main_menu, get_user_input, display_results

def main():
    while True:
        display_main_menu()
        choice = get_user_input()
        
        if choice == '1':
            display_results(list_all_files_and_dirs())
        elif choice == '2':
            file_name = input("Enter file name to create: ")
            display_results(create_file(file_name))
        elif choice == '3':
            file_name = input("Enter file name to delete: ")
            display_results(delete_file(file_name))
        elif choice == '4':
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            display_results(rename_file(old_name, new_name))
        elif choice == '5':
            file_name = input("Enter file name to edit: ")
            new_content = input("Enter new content: ")
            display_results(edit_file_content(file_name, new_content))
        elif choice == '6':
            query = input("Enter search query: ")
            display_results(search_file(query))
        elif choice == '7':
            file_name = input("Enter file name for details: ")
            display_results(file_details(file_name))
        elif choice == '8':
            file_name = input("Enter file name to sort content: ")
            display_results(sort_file_content(file_name))
        elif choice == '9':
            display_results(list_only_directories())
        elif choice == '10':
            extension = input("Enter file extension (e.g., .txt): ")
            display_results(list_files_of_extension(extension))
        elif choice == '11':
            display_results(count_directories())
        elif choice == '12':
            display_results(count_files())
        elif choice == '13':
            directory = input("Enter directory to sort files (default is current): ") or "."
            display_results(sort_files_in_directory(directory))
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
