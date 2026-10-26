#!/usr/bin/env python3
"""File organizer: moves files into subfolders based on their extension."""

import os
import shutil
import sys


def main() -> None:
    """Prompt for a folder path and organize files by type."""
    # Ask the user which folder to organize
    path: str = input("Enter the path of the folder to organize: ")

    # Validate that the path is an existing directory
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory or does not exist.")
        sys.exit(1)

    # Map category names to their file extensions
    FILE_TYPES: dict[str, list[str]] = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mov", ".avi"],
    }

    # Walk through every item in the folder
    for item in os.listdir(path):
        item_path: str = os.path.join(path, item)

        # Skip directories — only organize files
        if not os.path.isfile(item_path):
            continue

        # Extract the file extension (e.g., ".txt") and make it lowercase
        ext: str = os.path.splitext(item)[1].lower()

        # Check whether this extension belongs to any category
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                # Create the target subfolder if it doesn't yet exist
                target_dir: str = os.path.join(path, category)
                os.makedirs(target_dir, exist_ok=True)

                # Move the file into the matching subfolder
                shutil.move(item_path, os.path.join(target_dir, item))
                print(f"Moved {item} to {category}/")
                break  # stop checking other categories once matched


if __name__ == "__main__":
    main()
