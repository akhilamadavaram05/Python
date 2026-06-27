# Day 63 - Log Helper
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

def error_lines(lines):
    return [line for line in lines if "ERROR" in line]

def seed_sample():
    sample = """2026-06-27 10:00:01 INFO Server started
2026-06-27 10:00:05 DEBUG Checking config
2026-06-27 10:00:10 WARNING Disk space low
2026-06-27 10:00:15 ERROR Database connection failed
2026-06-27 10:00:20 INFO Retry successful
"""
    FILE.write_text(sample)

if __name__ == "__main__":
    seed_sample()
    lines = FILE.read_text().splitlines()
    print("Levels:", Counter(parse_levels(lines)))
    print("Errors:", error_lines(lines))