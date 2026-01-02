import fitz  # PyMuPDF

def pdf_to_ordered_text(pdf_path):
    doc = fitz.open(pdf_path)
    all_text = []

    for page in doc:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))  # y, x

        for block in blocks:
            text = block[4].strip()
            if text:
                all_text.append(text)

    return "\n".join(all_text)
