from pikepdf import Pdf

# Como combinar 2(ou mais) PDFs em um
pdf = Pdf.new()
fonte1 = Pdf.open('desafio_criar.pdf')
fonte2 = Pdf.open('desafio_tabela.pdf')

pdf.pages.extend(fonte1.pages)
pdf.pages.extend(fonte2.pages)

pdf.save('combinar_PDFs.pdf')

fonte1.close()
fonte2.close()
pdf.close()