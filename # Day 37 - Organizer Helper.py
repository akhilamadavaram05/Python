# Day 37 - Organizer Helper
import os
import shutil

def create_test_files(folder):
    """Create dummy files for testing."""
    os.makedirs(folder, exist_ok=True)
    examples = [
        ("image1.jpg", "Images"),
        ("doc.pdf", "Documents"),
        ("video.mp4", "Videos"),
        ("music.mp3", "Music"),
        ("archive.zip", "Archives"),
        ("script.py", "Others")
    ]
    for name, _ in examples:
        with open(os.path.join(folder, name), "w") as f:
            f.write("Dummy content")

def list_subfolders(path):
    """Show what folders were created."""
    print("Subfolders in", path, ":")
    for d in os.listdir(path):
        d_path = os.path.join(path, d)
        if os.path.isdir(d_path):
            print(f"  • {d} ({len(os.listdir(d_path))} files)")

if __name__ == "__main__":
    test_dir = "test_folder"
    create_test_files(test_dir)
    print("📊 Test files created in", test_dir)
    list_subfolders(test_dir)
    print("Now run organizer and re-check subfolders")