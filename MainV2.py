import timeit

from PyPDF2 import PdfReader, PdfWriter


def start():
    # 读取文件
    odd_pdf_reader = PdfReader("单数面.pdf")
    even_pdf_reader = PdfReader("偶数面.pdf")

    pdf_writer = PdfWriter()

    for odd_page, even_page in zip(odd_pdf_reader.pages, even_pdf_reader.pages[::-1]):
        pdf_writer.add_page(odd_page)
        pdf_writer.add_page(even_page)
    with open("output.pdf", "wb") as out:
        pdf_writer.write(out)


print("V2 cost time:")
print(timeit.timeit(start, number=1))
