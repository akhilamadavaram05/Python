# Day 64 - Server Helper
from pathlib import Path

HTML_FILE = Path("day64_index.html")

def check_html_file():
    if HTML_FILE.exists():
        print("✅ day64_index.html exists")
        content = HTML_FILE.read_text()
        print("Contains:", len(content), "chars")
    else:
        print("❌ day64_index.html not found")

if __name__ == "__main__":
    check_html_file()