import fitz


def merge_pdf(pdf_list, output_file_name):
    outlet = fitz.open()

    for pdf in pdf_list:
        with fitz.open(pdf) as pdfp:
            outlet.insert_pdf(pdfp)

    outlet.save(output_file_name)
