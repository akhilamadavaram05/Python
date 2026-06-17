# Day 52 - Test
from day52_helper import extract_emails, count_emails

def test_extract():
    text = "Contact a@b.com and user.name@test.org"
    emails = extract_emails(text)
    assert len(emails) == 2
    assert "a@b.com" in emails
    assert "user.name@test.org" in emails
    print("✅ Email extraction OK")

def test_count():
    text = "No emails here"
    assert count_emails(text) == 0
    text = "x@y.com"
    assert count_emails(text) == 1
    print("✅ Email count OK")
    print("Day 52 test ok")

test_extract()
test_count()