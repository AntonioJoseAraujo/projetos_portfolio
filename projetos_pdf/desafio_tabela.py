import csv
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("codigo.png", x=1, h=0.8)
        self.ln(0.1)
        self.set_font("helvetica", "B", 10)
        self.cell(w=0, h=0.5, text='DEV Antônio Araújo',
                  align='l', new_x='LMARGIN', new_y='NEXT')
        self.ln(0.1)
        self.set_font("helvetica", "B", 18)
        self.cell(0, 0, text="Relatório de Vendas",
                  align="c", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def colored_table(self, headings, rows, col_widths=(4.2, 3.9, 3.5)):
        self.set_fill_color(255, 100, 0)
        self.set_text_color(255)
        self.set_draw_color(255, 0, 0)
        self.set_line_width(0.03)
        self.set_font(style="B")
        for col_width, heading in zip(col_widths, headings):
            self.cell(col_width, 0.7, heading, border=1, align="C", fill=True)
        self.ln()
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font()
        fill = False
        for row in rows:
            self.cell(col_widths[0], 0.6, row[0],
                      border="LR", align="L", fill=fill)
            self.cell(col_widths[1], 0.6, row[1],
                      border="LR", align="L", fill=fill)
            self.cell(col_widths[2], 0.6, row[2],
                      border="LR", align="R", fill=fill)
            self.ln()
            fill = not fill
        self.cell(sum(col_widths), 0, "", "T")


def load_data_from_csv(csv_filepath):
    headings, rows = [], []
    with open(csv_filepath, encoding="utf8") as csv_file:
        for row in csv.reader(csv_file, delimiter=";"):
            if not headings:
                headings = row
            else:
                rows.append(row)
    return headings, rows


americ, dados = load_data_from_csv("carros_americanos.csv")
itali, dados_ita = load_data_from_csv("carros_italianos.csv")

pdf = PDF(unit='cm')
pdf.set_font("helvetica", size=12)
pdf.add_page()
pdf.cell(w=0, h=1, text='Para o mês de dezembro, foram registrados um total de 10 vendas para o setor de veículos importados',
         new_x='LMARGIN', new_y='next')

pdf.set_font("helvetica", "b", size=15)
pdf.cell(w=0, h=1, text='Vendas de carros americanos',
         new_x='LMARGIN', new_y='next')

pdf.set_font("helvetica", size=12)
pdf.cell(w=0, h=0.5, text='Foram vendidos 5 carros americanos',
         new_x='LMARGIN', new_y='next')
pdf.colored_table(americ, dados)
pdf.ln()
pdf.set_font("helvetica", "b", size=15)
pdf.cell(w=0, h=1, text='Vendas de carros italianos',
         new_x='LMARGIN', new_y='next')

pdf.set_font("helvetica", size=12)
pdf.cell(w=0, h=0.5, text='Foram vendidos 5 carros italianos',
         new_x='LMARGIN', new_y='next')
pdf.colored_table(itali, dados_ita)
pdf.set_author("Antônio Araújo")
pdf.output("desafio_tabela.pdf")
