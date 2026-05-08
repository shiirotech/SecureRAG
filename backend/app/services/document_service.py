from pypdf import PdfReader

def extract_text(path):
    if path.endswith("pdf"):
        return extract_pdf_text(path)

    elif path.endswith("txt"):
        return extract_txt_text(path)
    
    else:
        return []

def extract_pdf_text(path):
    reader = PdfReader(path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""

        pages.append({
            "text": text,
            "page": i + 1
        })

    return pages

def extract_txt_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
        
    return [{
        "page": 1,
        "text": text
    }]