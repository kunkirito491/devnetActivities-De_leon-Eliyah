"""
Module 2 — Activity: File Sorting with os and shutil
Student: De leon, Eliyah Rieluis J.
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

I made a simple file sorter using os and shutil. It checks the files in a folder and moves them into different folders based on their file extension, like .txt, .jpg, and .pdf.

============================================
KEY VOCABULARY
============================================
- os module: Used for working with files and folders.
- shutil module: Used for moving and copying files.
- file path: The location of a file on the computer.
- directory: Another name for a folder.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---

folder = "test_folder"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension:
            new_folder = os.path.join(folder, extension[1:] + "_files")
            os.makedirs(new_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(new_folder, file))

print("Files sorted successfully!")      

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

One mistake I could make is using the wrong folder path. If the folder doesn't exist, the program won't work. I learned to check the folder name and path first.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

This is similar to real automation because the computer can organize files for me instead of doing everything manually. It can save time when there are many files to sort.
"""
