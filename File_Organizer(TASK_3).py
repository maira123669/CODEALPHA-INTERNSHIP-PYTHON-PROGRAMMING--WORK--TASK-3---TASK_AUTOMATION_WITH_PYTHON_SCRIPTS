import os
import shutil
from tkinter import Tk, filedialog

def organize_folder():
    # 1. Open a native Windows folder picker dialog
    root = Tk()
    root.withdraw() # Hide the main blank tkinter window
    root.attributes('-topmost', True) # Bring the folder picker to the front
    
    print("Select the folder you want to organize in the Windows pop-up...")
    target_dir = filedialog.askdirectory(title="Select Folder to Organize")
    
    if not target_dir:
        print(" No folder selected. Exiting.")
        return

    print(f"\nScanning: {target_dir}")

    # 2. Define the categories and their associated extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".tar", ".gz"]
    }

    moved_files_count = 0

    # 3. Scan the selected directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # Skip directories, only process files
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g., '.jpg')
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find matching folder category
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                # Create the destination folder inside the selected directory if it doesn't exist
                dest_folder = os.path.join(target_dir, folder_name)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                # Move the file
                dest_path = os.path.join(dest_folder, filename)
                try:
                    shutil.move(file_path, dest_path)
                    print(f"📁 Moved: {filename} ➡️ {folder_name}/")
                    moved_files_count += 1
                except Exception as e:
                    print(f"⚠️ Could not move {filename}: {e}")
                break # Stop checking other categories for this file

    print(f"\n✅ Success! Organized {moved_files_count} files successfully on your Windows drive.")

if __name__ == "__main__":
    organize_folder()
