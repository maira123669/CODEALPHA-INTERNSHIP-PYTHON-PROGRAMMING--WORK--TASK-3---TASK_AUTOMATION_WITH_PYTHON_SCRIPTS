#  File Organizer (Python)

##  Project Description

The **File Organizer** is a Python desktop application that automatically organizes files into categorized folders based on their file extensions. The program allows the user to select a folder using a graphical folder picker and then sorts files into folders such as **Images**, **Documents**, **Videos**, and **Archives**.

This project demonstrates the use of Python's file handling, directory management, GUI integration with Tkinter, and automation techniques.

---

##  Features

- Graphical folder selection using **Tkinter**.
- Automatically scans the selected directory.
- Organizes files based on their extensions.
- Creates folders automatically if they do not exist.
- Moves files into appropriate categories.
- Displays progress and success messages.
- Handles errors during file operations.

---

##  Technologies Used

- Python 3
- Tkinter (GUI)
- OS Module
- Shutil Module

---

##  Project Structure

```
File-Organizer/
│── file_organizer.py
│── README.md
```

---

##  How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python file_organizer.py
```

5. A folder selection window will appear.
6. Choose the folder you want to organize.
7. The program will automatically sort supported files into categorized folders.

---

##  Supported File Categories

| Folder | File Extensions |
|---------|-----------------|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| **Documents** | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx` |
| **Videos** | `.mp4`, `.mkv`, `.mov`, `.avi` |
| **Archives** | `.zip`, `.rar`, `.tar`, `.gz` |

---

##  How It Works

1. Opens a folder selection dialog.
2. Scans all files in the selected folder.
3. Detects each file's extension.
4. Matches the extension with a predefined category.
5. Creates category folders if they do not already exist.
6. Moves files into their respective folders.
7. Displays a summary of the organized files.

---

##  Concepts Used

- Functions
- File Handling
- Directory Management
- OS Module
- Shutil Module
- Tkinter GUI
- Loops
- Conditional Statements
- Exception Handling

---

##  Future Improvements

- Support additional file types.
- Add custom user-defined categories.
- Organize files into subfolders based on date.
- Add drag-and-drop support.
- Create a graphical user interface (GUI) with progress indicators.
- Add an option to undo file organization.

---

##  Author

**Maira Masood**

BS Computer Science (BSCS)

---

##  License

This project is created for learning and educational purposes.
