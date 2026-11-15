from pathlib import Path
import shutil
from datetime import datetime

# 1. Define the path to the folder we are organizing
target_directory = Path("./test_downloads")
target_directory.mkdir(exist_ok=True)

# 2. Define our File Categories mapping
FILE_CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Media": [".mp4", ".mp3", ".wav", ".mov", ".mkv"]
}


def get_category(extension):
    """Given a file extension, returns the matching category name."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_downloads():
    print(f"Organizing directory: {target_directory.resolve()}\n")

    # Path for our log file inside the target directory
    log_path = target_directory / "organizer_log.txt"

    file_count = 0
    # Open log file in append mode ('a') so we keep past logs
    with open(log_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n--- Run at {timestamp} ---\n")

        for item in target_directory.iterdir():
            if item.is_file():
                # Skip our script and the log file itself
                if item.name in ["organizer.py", "organizer_log.txt"]:
                    continue

                file_extension = item.suffix.lower()
                category = get_category(file_extension)

                # Create category folder if it doesn't exist
                category_folder = target_directory / category
                category_folder.mkdir(exist_ok=True)

                destination_path = category_folder / item.name

                # Handle duplicate file names safely
                if destination_path.exists():
                    base_name = item.stem
                    suffix = item.suffix
                    counter = 1
                    while destination_path.exists():
                        new_filename = f"{base_name}_{counter}{suffix}"
                        destination_path = category_folder / new_filename
                        counter += 1

                # Move the file
                shutil.move(str(item), str(destination_path))

                log_message = f"Moved: {item.name} -> {category}/{destination_path.name}"
                print(log_message)
                log_file.write(log_message + "\n")
                file_count += 1

    print(
        f"\n✨ Done! Successfully organized {file_count} files. Activity logged.")


if __name__ == "__main__":
    organize_downloads()
