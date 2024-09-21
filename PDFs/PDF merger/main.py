from PyPDF2 import PdfMerger as merg
from os import curdir as dir, listdir as lis, makedirs, path

output_dir = path.join(dir, "Merged pdf")
makedirs(output_dir, exist_ok=True)

m = merg()

for f in lis(dir):
    if f.endswith(".pdf"):
        m.append(f)

m.write(path.join(output_dir, "Merged.pdf"))
