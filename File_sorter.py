import os
import shutil
from pathlib import Path

# Define the file categories and their associated extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.doc', '.xls'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.sh', '.bat', '.html', '.css'],
    'Executables': ['.exe', '.msi', '.apk', '.bin', '.dmg']
}

# Function to sort files in a given directory
def sort_files(directory):
    # Ensure the provided directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Iterate over files in the directory
    for file_name in os.listdir(directory):  # Make sure the indentation is correct here
        file_path = os.path.join(directory, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Extract the file extension
        file_extension = Path(file_name).suffix.lower()
        
        # Check which category the file belongs to
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                # Create the category folder if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(category_folder, file_name))
                print(f"Moved: {file_name} to {category}")
                moved = True
                break
        
        # If no category is found, move the file to an "Others" folder
        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, file_name))
            print(f"Moved: {file_name} to Others")

# Main function to execute the script
def main():
    folder_to_sort = input("Enter the path of the folder to sort: ").strip()
    sort_files(folder_to_sort)
    print("File sorting complete!")

if __name__ == '__main__':
    main()
