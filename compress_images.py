"""
Compress all images for the AGNIverse website.
- Gallery images: resize to max 1200px wide, JPEG quality 72
- Logo: resize to max 600px wide, optimize PNG
- Maps icon: resize to max 100px, optimize PNG
"""
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))

def compress_jpeg(path, max_width=1200, quality=72):
    orig_size = os.path.getsize(path)
    img = Image.open(path)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    w, h = img.size
    if w > max_width:
        ratio = max_width / w
        new_h = int(h * ratio)
        img = img.resize((max_width, new_h), Image.LANCZOS)
    img.save(path, 'JPEG', quality=quality, optimize=True)
    new_size = os.path.getsize(path)
    saved = orig_size - new_size
    pct = (saved / orig_size) * 100 if orig_size > 0 else 0
    print(f"  {os.path.basename(path)}: {orig_size//1024}KB -> {new_size//1024}KB (saved {pct:.1f}%)")
    return saved

def compress_png(path, max_width=600):
    orig_size = os.path.getsize(path)
    img = Image.open(path)
    w, h = img.size
    if w > max_width:
        ratio = max_width / w
        new_h = int(h * ratio)
        img = img.resize((max_width, new_h), Image.LANCZOS)
    img.save(path, 'PNG', optimize=True)
    new_size = os.path.getsize(path)
    saved = orig_size - new_size
    pct = (saved / orig_size) * 100 if orig_size > 0 else 0
    print(f"  {os.path.basename(path)}: {orig_size//1024}KB -> {new_size//1024}KB (saved {pct:.1f}%)")
    return saved

total_saved = 0

print("\n=== GALLERY IMAGES ===")
gallery_dir = os.path.join(BASE, "gallery")
for f in sorted(os.listdir(gallery_dir)):
    if f.lower().endswith(('.jpg', '.jpeg')):
        total_saved += compress_jpeg(os.path.join(gallery_dir, f), max_width=1200, quality=72)

print("\n=== LOGO ===")
logo_path = os.path.join(BASE, "logo", "Agniverse Logo.png")
if os.path.exists(logo_path):
    total_saved += compress_png(logo_path, max_width=600)

print("\n=== MAPS ICON ===")
maps_path = os.path.join(BASE, "logo", "maps-icon.png")
if os.path.exists(maps_path):
    total_saved += compress_png(maps_path, max_width=100)

print(f"\n{'='*40}")
print(f"TOTAL SAVED: {total_saved / 1024 / 1024:.1f} MB")
print(f"{'='*40}")
