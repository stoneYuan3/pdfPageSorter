from pypdf import PdfWriter, PdfReader
output_pdf = PdfWriter()

with open(r'target.pdf', 'rb') as readfile:
    input_pdf = PdfReader(readfile)
    total_pages = len(input_pdf.pages)
    print(total_pages)
    for page in range(0 , total_pages , 4):
        print(page)
        print("pg+3 " + str(page+3))

        #pg.1
        output_pdf.add_page(input_pdf.pages[page])
        print("page0 active")
        
        #pg.4
        if page+3 < total_pages:
            output_pdf.add_page(input_pdf.pages[page+3])
            print("page+2 active")

        #pg.3
        if page+2 < total_pages:
            output_pdf.add_page(input_pdf.pages[page+2])
            print("page+3 active")

        #pg.2
        if page+1 < total_pages:
            output_pdf.add_page(input_pdf.pages[page+1])
            print("page+1 active")
            
            
    with open(r'output.pdf', "wb") as writefile:
        output_pdf.write(writefile)
