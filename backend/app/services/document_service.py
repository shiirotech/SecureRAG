from pypdf import PdfReader

def extract_text(path):
    reader = PdfReader(path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        pages.append({
            "text": text,
            "page": i + 1
        })

    return pages