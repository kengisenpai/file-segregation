import os
import shutil
import argparse

# Define file extensions mapping
FILE_CATEGORIES = {
    "Excel_Files": [".xls", ".xlsx", ".xlsb", ".xlsm", ".ods", ".csv"],
    "Word_Files": [".doc", ".txt", ".rtf", ".domt", ".dotx", ".docx"],
    "PowerPoint_Files": [".ppt", ".pptm", ".pptx"],
    "onenote": [".one", ".onepkg", ".onemodel"],
    "Accessfiles": [".access", ".mdb", ".ldb"],
    "Html&Xml": [".htm", ".html", ".xml"],
    "Scandocs_fiels": [".jpeg", ".jpg", ".gif", ".bmp", ".png", ".heic"],
    "PDF_Files": [".pdf"]
}

def segregate_files(source_directory, destination_directory):
    """ Segregates files into categorized folders inside the destination directory. """
    
    # Check if source directory exists
    if not os.path.exists(source_directory):
        print(f"Error: The source directory '{source_directory}' does not exist.")  
        return

    # Create destination directory if it does not exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Loop through files in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to respective folder
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                folder_path = os.path.join(destination_directory, folder)

                # Create subfolder in the destination directory if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move file to respective folder in the destination
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} → {folder}/")
                moved = True
                break

        if not moved:
            print(f"Skipped: {filename} (Unknown file type)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Segregation Script")
    parser.add_argument("source_directory", type=str, help="Path of the directory containing files")
    parser.add_argument("destination_directory", type=str, help="Path of the directory where files will be moved")

    args = parser.parse_args()
    segregate_files(args.source_directory, args.destination_directory)
