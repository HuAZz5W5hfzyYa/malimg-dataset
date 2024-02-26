import os

def count_files_in_subdirectories(directory='.'):
    for subdir, dirs, files in os.walk(directory):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Count non-hidden files in the current subdirectory
        file_count = len([f for f in files if not f.startswith('.')])
        
        # Print directory name and file count
        print(f"{subdir}: {file_count}")

# Call the function with the current directory
count_files_in_subdirectories()
