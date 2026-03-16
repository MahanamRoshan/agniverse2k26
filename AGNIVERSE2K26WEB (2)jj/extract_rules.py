import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespaces
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_parts = []
            for paragraph in tree.findall('.//w:p', ns):
                paragraph_text = ""
                for run in paragraph.findall('.//w:r', ns):
                    text = run.find('.//w:t', ns)
                    if text is not None and text.text:
                        paragraph_text += text.text
                if paragraph_text:
                    text_parts.append(paragraph_text)
                else:
                    text_parts.append("[Empty Paragraph]")
            
            return "\n".join(text_parts)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    path = "AGNIVERSE '26 Event Rules and Regulations.docx"
    print(extract_text(path))
