print("Hello, World!")
import sys
import os

print("Python Path:", sys.path)
print("Current Folder:", os.getcwd())

import _backup as backup
import file_utils
import logger

SOURCE_FOLDER = "source"
DEST_FOLDER = "backup"


def menu():
    print("\n===== AUTOMATION SYSTEM =====")
    print("1. Run Backup")
    print("2. Exit")


def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            backup.run_backup(SOURCE_FOLDER, DEST_FOLDER, file_utils, logger)

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
  
