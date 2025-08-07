import fitz  # PyMuPDF


async def parse_resume(resume_file):
    content = await resume_file.read()
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
