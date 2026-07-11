import os
import shutil

# Source folder (where .jpg files are located)
source_folder = r"C:\PROJECTS\CodeAlpha_PythonProgramming\Task Automation\Source"

# Destination folder (where you want to move them)
destination_folder = r"C:\PROJECTS\CodeAlpha_PythonProgramming\Task Automation\Destination"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source folder
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        
        # Move file
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

print("All .jpg files moved successfully!")