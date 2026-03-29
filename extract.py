import zipfile
import xml.etree.ElementTree as ET
import sys

def extract(docx_path):
    try:
        doc = zipfile.ZipFile(docx_path)
        xml_content = doc.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        text_runs = []
        for paragraph in tree.findall('.//w:p', ns):
            texts = [node.text for node in paragraph.findall('.//w:t', ns) if node.text]
            if texts:
                text_runs.append(''.join(texts))
        
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_runs))
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract('Latihan_Bab2.docx')
