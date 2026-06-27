# Day 63 - Test
from day63_helper import seed_sample, parse_levels, error_lines, FILE

def test_log_analysis():
    seed_sample()
    lines = FILE.read_text().splitlines()
    levels = parse_levels(lines)
    assert levels.count("INFO") == 2
    assert levels.count("DEBUG") == 1
    assert levels.count("WARNING") == 1
    assert levels.count("ERROR") == 1
    assert len(error_lines(lines)) == 1
    print("✅ Log analysis OK")
    print("Day 63 test ok")

test_log_analysis()