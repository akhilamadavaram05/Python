# Day 63 - Log File Analyzer (MAIN)
from collections import Counter
from pathlib import Path
import re

FILE = Path("day63_sample.log")

def parse_levels(lines):
    levels = []
    for line in lines:
        m = re.search(r'\b(INFO|WARNING|ERROR|DEBUG)\b', line)
        if m:
            levels.append(m.group(1))
    return levels

def main():
    sample = """2026-06-27 10:00:01 INFO Server started
2026-06-27 10:00:05 DEBUG Checking config
2026-06-27 10:00:10 WARNING Disk space low
2026-06-27 10:00:15 ERROR Database connection failed
2026-06-27 10:00:20 INFO Retry successful
"""
    FILE.write_text(sample)
    print("Created day63_sample.log")

    lines = FILE.read_text().splitlines()
    levels = parse_levels(lines)
    counts = Counter(levels)

    print("Log level counts:")
    for level in ["INFO", "DEBUG", "WARNING", "ERROR"]:
        print(f"{level}: {counts.get(level, 0)}")

if __name__ == "__main__":
    main()