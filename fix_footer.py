#!/usr/bin/env python3
"""Fix the corrupted base64 blob in index.html footer at line 5878."""

import sys

input_file = 'index.html'
output_file = 'index_fixed.html'

copyright_html = '''        <div class="footer-bottom">
            <div class="footer-bottom-inner">
                <p class="footer-copyright">
                    &copy; 2026 <strong>AGNIverse</strong>. All rights reserved. Made with 
                    <span class="footer-heart">&#10084;</span> by the AGNIverse Team.
                </p>
                <div class="footer-bottom-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Use</a>
                    <a href="#">Contact</a>
                </div>
            </div>
        </div><!-- /.container -->
    </footer><!-- /#footer -->'''

lines_processed = 0
corrupt_found = False

with open(input_file, 'r', encoding='utf-8', errors='replace') as reader, \
     open(output_file, 'w', encoding='utf-8') as writer:
    for line_num, line in enumerate(reader, start=1):
        if line_num == 5878:
            # Check if this line starts with the corrupted content
            stripped = line.strip()
            if stripped.startswith('<div class="container">AAAQ') or \
               stripped.startswith('<div class="container">'):
                # Check if it's absurdly long (corruption indicator)
                if len(line) > 500:
                    print(f"Found corrupt line {line_num}, length={len(line):,} chars")
                    corrupt_found = True
                    writer.write(copyright_html + '\n')
                else:
                    writer.write(line)
            else:
                print(f"Line 5878 preview: {line[:100]}")
                writer.write(line)
        else:
            writer.write(line)
        lines_processed = line_num

print(f"Done. Lines processed: {lines_processed:,}")
print(f"Corrupt line found and fixed: {corrupt_found}")
