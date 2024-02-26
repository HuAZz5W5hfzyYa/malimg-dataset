import os
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_images(directory):
    image_hashes = {}
    duplicate_count = 0

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_hash = get_file_hash(file_path)
                if file_hash in image_hashes:
                    duplicate_count += 1
                else:
                    image_hashes[file_hash] = file_path

    return duplicate_count, image_hashes

def main():
    current_directory = os.getcwd()
    
    # Print Markdown table header
    print("| Directory | Files | Duplicates | Files After Removing Duplicates |")
    print("|------------|-------|-------------|-------------------------------|")

    for root, dirs, files in os.walk(current_directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]  # Exclude hidden directories
        for directory in dirs:
            directory_name = os.path.join(root, directory).split(os.path.sep)[-1]
            directory_path = os.path.join(root, directory)
            files_count = len(os.listdir(directory_path))
            duplicates, _ = find_duplicate_images(directory_path)
            files_after_removing_duplicates = files_count - duplicates
            
            # Print row in the Markdown table
            print(f"| {directory_name} | {files_count} | {duplicates} | {files_after_removing_duplicates} |")

if __name__ == "__main__":
    main()
