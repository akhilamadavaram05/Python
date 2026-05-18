# Day 37 - File Organizer (CLI)
import os
import shutil

def organize_folder(path):
    """Organize files in path into folders by type."""
    if not os.path.exists(path):
        print("❌ Path does not exist")
        return
    if not os.path.isdir(path):
        print("❌ Not a directory")
        return
        
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".txt", ".docx", ".pptx", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
    }
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1].lower()
            moved = False
            for cat, exts in categories.items():
                if ext in exts:
                    cat_folder = os.path.join(path, cat)
                    os.makedirs(cat_folder, exist_ok=True)
                    shutil.move(item_path, os.path.join(cat_folder, item))
                    print(f"Moved {item} → {cat}/")
                    moved = True
                    break
            if not moved:
                others = os.path.join(path, "Others")
                os.makedirs(others, exist_ok=True)
                shutil.move(item_path, os.path.join(others, item))
                print(f"Moved {item} → Others/")

if __name__ == "__main__":
    target = input("Enter folder path to organize (e.g. Downloads): ")
    organize_folder(target)