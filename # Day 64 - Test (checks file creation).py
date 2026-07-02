# Day 64 - Test (checks file creation)
from day64_helper import check_html_file, HTML_FILE

def test_html_file():
    # Just check that file exists (we assume user ran day64.py before test)
    assert HTML_FILE.exists()
    content = HTML_FILE.read_text()
    assert "Day 64" in content
    print("✅ HTML file OK")
    print("Day 64 test ok")

test_html_file()