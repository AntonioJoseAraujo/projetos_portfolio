from fpdf import FPDF

pdf = FPDF(orientation='p', unit='cm', format='a4')

pdf.add_page()

pdf.set_font("helvetica", "b", 20)
pdf.cell(w=0, h=2, text='Relatório de Vendas',
         align='c', new_x='LMARGIN', new_y='next')

pdf.set_font("helvetica", size=12)
pdf.cell(w=0, h=1, text='Para o mês de dezembro, foram registrados um total de 190 vendas para o setor de veículos importados',
         new_x='LMARGIN', new_y='next')

pdf.set_font("helvetica", "b", size=15)
pdf.cell(w=0, h=1, text='Vendas de carros americanos',
         new_x='LMARGIN', new_y='next')

pdf.set_font('helvetica', size=12)
pdf.cell(w=0, h=0.5, text='Foram vendidos 100 carros americanos',
         new_x='LMARGIN', new_y='next')

pdf.ln(0.5)

pdf.set_font("helvetica", "b", size=15)
pdf.cell(w=0, h=1, text='Vendas de carros italianos',
         new_x='LMARGIN', new_y='next')

pdf.set_font('helvetica', size=12)
pdf.cell(w=0, h=0.5, text='Foram vendidos 90 carros italianos',
         new_x='LMARGIN', new_y='next')

pdf.output("desafio_criar.pdf")
