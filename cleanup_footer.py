#!/usr/bin/env python3
"""Remove the orphaned old footer HTML from the fixed file (lines 5892-5903)."""

import sys

input_file = 'index_fixed.html'
output_file = 'index.html'

# These are 1-indexed line numbers to REMOVE (the old footer remnants)
# Lines 5892-5903 are the orphaned old footer content that shouldn't be there
REMOVE_START = 5892
REMOVE_END = 5903  # inclusive

lines_removed = 0
output_lines = 0

with open(input_file, 'r', encoding='utf-8', errors='replace') as reader, \
     open(output_file, 'w', encoding='utf-8') as writer:
    for line_num, line in enumerate(reader, start=1):
        if REMOVE_START <= line_num <= REMOVE_END:
            # Skip this line (old footer remnants)
            lines_removed += 1
        else:
            writer.write(line)
            output_lines += 1

print(f"Done! Input lines processed, {lines_removed:,} orphaned lines removed.")
print(f"Output file has {output_lines:,} lines.")
