import markdown
from docx import Document
from htmldocx import HtmlToDocx

def read_md():
    with open('./test-data/markdown_sample.md', 'r') as f:
        text = f.read()
    return markdown.markdown(text)

def write_doc(text):
    doc = Document()
    parser = HtmlToDocx()
    parser.add_html_to_document(text, doc)

    doc.save("./test-data/markdown_sample.docx")

if __name__=="__main__":
    write_doc(read_md())