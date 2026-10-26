# File Organizer CLI

## Description

File Organizer CLI is a simple command-line tool that sorts files in a given
folder into categorized subfolders based on their file extensions.
It currently supports the following categories and extensions:

- **Images** — `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents** — `.pdf`, `.txt`, `.docx`
- **Videos** — `.mp4`, `.mov`, `.avi`

Files whose extensions do not match any category are left in place.

## Requirements

- **Python 3.x** (3.6 or later)

No external packages are required. The script uses only the standard-library
modules `os`, `shutil`, and `sys`.

## Usage

Run the script from your terminal:

```bash
python organizer.py
```

The script will prompt you for the path of the folder to organize. A typical
session looks like this:

```bash
$ python organizer.py
Enter the path of the folder to organize: ./test_folder
Moved photo.jpg to Images/
Moved report.pdf to Documents/
Moved clip.mp4 to Videos/
Moved notes.txt to Documents/
```

After running, the folder will contain the subfolders `Images/`, `Documents/`,
and `Videos/` (created automatically if they do not already exist), each
holding the files that matched the corresponding category.

## Project Structure

```
Intro_to_AI_mini_proj2/
├── organizer.py      # Main script – the file organizer
├── test_folder/      # Example folder for testing
│   ├── Images/       # (created on first run)
│   ├── Documents/    # (created on first run)
│   └── Videos/       # (created on first run)
└── README.md         # This file
```
