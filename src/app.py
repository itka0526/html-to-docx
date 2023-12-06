from .utils import read_html_from_str, save_file, html_to_docx


def convert_html_to_docx(path):
    obj = read_html_from_str(path)
    doc = html_to_docx(obj)
    new_path = path.split(".")[0] + ".docx"
    save_file(doc, new_path)


def run():
    import sys
    if len(sys.argv) != 2:
        print("Usage: html_to_docx <HTML_FILE_PATH>")
        sys.exit(1)

    input_path = sys.argv[1]
    convert_html_to_docx(input_path)


if __name__ == "__app__":
    run()
