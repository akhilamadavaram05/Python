# Day 37 - Test
import os
import shutil
from day37 import organize_folder

def setup_test_dir(dirname="test_organize"):
    """Create test structure."""
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.makedirs(dirname)
    for name in ("file.jpg", "file.pdf", "file.mp4", "file.mp3", "file.zip", "script.py"):
        with open(os.path.join(dirname, name), "w") as f:
            f.write("test")
    return dirname

def test_file_organize():
    folder = setup_test_dir()
    print("📁 Test dir ready, organizing...")
    organize_folder(folder)
    
    # Check categories exist and have files
    for cat in ("Images", "Documents", "Videos", "Music", "Archives", "Others"):
        cat_path = os.path.join(folder, cat)
        assert os.path.exists(cat_path), f"{cat} folder missing"
        assert len(os.listdir(cat_path)) > 0, f"{cat} empty"
    print("✅ File organize tests OK")
    print("Day 37 test ok")

if __name__ == "__main__":
    test_file_organize()