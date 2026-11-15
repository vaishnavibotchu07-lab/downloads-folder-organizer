# Automated Downloads Folder Organizer

A simple, efficient Python automation script designed to clean up messy directories (like your Downloads folder) by automatically sorting files into categorized subfolders with duplicate-name safety and permanent logging.

## Features :
* **Auto-Categorization:** Instantly sorts files into dedicated folders (`Images`, `Documents`, `Code`, `Archives`, `Media`, and `Others`) based on their file extensions.
* **Duplicate-Name Safety:** Prevents data loss or errors by automatically detecting existing file names and appending an incremented counter (e.g., `report_1.pdf`).
* **Timestamped Logging:** Generates a permanent activity log (`organizer_log.txt`) tracking every file movement with precise timestamps.
* **Cross-Platform Compatibility:** Built using Python's modern `pathlib` module to work seamlessly across Windows, macOS, and Linux.

## Tech Stack :
* **Language:** Python 3.x
* **Modules Used:** `pathlib`, `shutil`, `datetime`

## How to run it :
1. Clone this repository or download `organizer.py`.
2. Open your terminal or command prompt inside the project folder.
3. Run the script:
   ```bash
   python organizer.py

   Built by B. Vaishnavi as part of my Python automation journey.
