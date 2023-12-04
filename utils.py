from pandas import read_html
from docx import Document


def read_html_from_str(io):
    df = read_html(io, encoding="utf-8")[0]
    d = df.to_dict(orient="tight")["data"]
    return d


def html_to_docx(d):
    max_col_length = len(d[0])

    doc = Document()
    table = doc.add_table(rows=0, cols=max_col_length)

    table.style = "Table Grid"

    for row_data in d:
        row_cells = table.add_row().cells
        for i, cell_data in enumerate(row_data):
            row_cells[i].text = cell_data

    return doc


def save_file(doc, file_name):
    doc.save(file_name)
    print("File saved to: " + file_name)
