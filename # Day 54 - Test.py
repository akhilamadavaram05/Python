# Day 54 - Test
from day54_helper import extract_urls, count_urls

def test_extract():
    text = "Go to https://example.com and http://test.org/page"
    urls = extract_urls(text)
    assert len(urls) == 2
    assert "https://example.com" in urls
    assert "http://test.org/page" in urls
    print("✅ URL extraction OK")

def test_count():
    text = "No URLs here"
    assert count_urls(text) == 0
    text = "Visit https://x.com"
    assert count_urls(text) == 1
    print("✅ URL count OK")
    print("Day 54 test ok")

test_extract()
test_count()