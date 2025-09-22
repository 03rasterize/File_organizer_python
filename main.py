'''
---------------------
File Organizer Script
---------------------
This script organizes files in a folder depending on their extension,
it moves them into subfolders after the file type.
Like .png .pdf. ai .psd etc
'''
import os
import shutil


def organize_files(folder_path):
    files_moved = 0
    
    for file in os.listdir(folder_path):
        filepath = os.path.join(folder_path, file)
        
        if os.path.isfile(filepath):
            file_extension = os.path.splitext(file)[1].lower()
            
            target_folder = os.path.join(folder_path, file_extension[1:] if file_extension else 'others')
            os.makedirs(target_folder, exist_ok=True)
        
            shutil.move(filepath, os.path.join(target_folder, file))
            files_moved += 1
    
    print(f'Files organized!⭐ Number of files moved: {files_moved}')
    
def main():
    
    folder = './downloads'
    
    if not os.path.exists(folder):
        print(f"Error: The folder '{folder}' does NOT exist.")
        return
    
    organize_files(folder)
    
if __name__ == '__main__':
    main()