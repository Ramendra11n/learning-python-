import PyPDF2 

filename='sample.pdf'
# creating the binary file
pdfb=open(filename,'rb')
# creating the PDF content
pdf_reader=PyPDF2.PdfReader(pdfb)

no_of_pages=len(pdf_reader.pages)

for x in range(no_of_pages):
  page=pdf_reader.pages[x]
  content =page.extract_text()
  print(content)
  print('\n')
  
