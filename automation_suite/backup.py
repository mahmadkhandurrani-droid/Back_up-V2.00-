print("Hello, World!")
import os
import shutil
from datetime import datetime


ALLOWED_EXTENSIONS = (".txt", ".jpg")


def is_allowed(file_name):
    return file_name.endswith(ALLOWED_EXTENSIONS)


def run_backup(source_folder, dest_folder, file_utils, logger):

    if not os.path.exists(source_folder):
        logger.log("Source folder not found")
        print("Source folder not found!")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(dest_folder, f"backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    copied = 0
    skipped = 0

    for item in file_utils.list_files(source_folder):
        full_path = file_utils.join_path(source_folder, item)

        if file_utils.is_file(full_path) and is_allowed(item):
            try:
                shutil.copy2(full_path, backup_path)
                logger.log(f"Copied: {item}")
                copied += 1
            except Exception as e:
                logger.log(f"Error: {item} -> {e}")
                skipped += 1
        else:
            skipped += 1

    logger.log(f"Backup done. Copied={copied}, Skipped={skipped}")

    print("\n--- SUMMARY ---")
    print("Copied:", copied)
    print("Skipped:", skipped)
