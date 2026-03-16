import base64
import os
import re
import urllib.parse

def get_base64(path):
    mime_type = "image/png" if path.lower().endswith(".png") else "image/jpeg"
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:{mime_type};base64,{encoded_string}"

def process_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all image paths in the HTML
    
    # regex to find potential image paths in src or imgSrc
    # Supports both quoted and unquoted (though unquoted is rare in HTML)
    pattern = r'(src|imgSrc|href)\s*[:=]\s*["\'](.*?/.*?\.(png|jpeg|jpg))["\']'
    
    matches = list(re.finditer(pattern, content))
    print(f"Found {len(matches)} potential images.")

    for match in matches:
        orig_path = match.group(2)
        # Unquote URL (e.g., %20 -> space)
        img_path = urllib.parse.unquote(orig_path)
        
        if os.path.exists(img_path):
            print(f"Embedding: {img_path}")
            b64 = get_base64(img_path)
            # Replace the EXACT original string from the HTML
            content = content.replace(f'"{orig_path}"', f'"{b64}"')
            content = content.replace(f"'{orig_path}'", f"'{b64}'")
        else:
            print(f"File not found: {img_path}")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    process_html("index.html")
