from utils import read_html_from_str, save_file, html_to_docx


path = input("Enter the HTML file's directory: \n ")
obj = read_html_from_str(path)
doc = html_to_docx(obj)
new_path = path.split(".")[0] + ".docx"
save_file(doc, new_path)
print("File saved to ", new_path)
