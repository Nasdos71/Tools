from docx2pdf import convert as conv
from os import curdir as dir, listdir as lis, makedirs, path

output_dir = path.join(dir, "Pdfs")
makedirs(output_dir, exist_ok=True)

for f in lis(dir):
    if f.endswith(".docx"):
        input_path = path.abspath(path.join(dir, f))
        out = path.join(output_dir, f.split('.')[0] + '.pdf')
        conv(input_path=input_path, output_path=out)

