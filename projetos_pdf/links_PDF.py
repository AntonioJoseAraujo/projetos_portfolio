from fpdf import FPDF, HTMLMixin


class MyFPDF(FPDF, HTMLMixin):
    pass


pdf = MyFPDF()

# First page:
pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5, "Clique aqui para ir para a próxima página ")
pdf.set_font(style="U")
link = pdf.add_link()
pdf.write(h=5, text="aqui", link=link)
pdf.set_font()

# Second page:
pdf.add_page()
pdf.set_link(link)
pdf.image(
    "computadores.png", 10, 10, 50, 0, "", "www.devaprender.com") 
pdf.set_left_margin(65)
pdf.set_font_size(18)
pdf.write_html(
    """<h1>Dev Aprender</h1>
<p>Para aprender a programar, tem que ser curioso. Para aprender a programar, tem que ser curioso. Para aprender a programar, tem que ser curioso. </p>
<p>*Texto ilustrativo, podemos colocar vários parágrafos aqui</p>
<p>Aqui no ícone temos o link do professor, podendo ter qualquer outro link(deixei esse link pois ainda não criei minha página para portfólio) e logo a baixo um link para a google.</p>
<p>Além de <b>curioso</b> deve saber <i>pesquisar</i></p>
<p>O site que todos devem saber utilizar é o <a href="https://www.google.com">google.</a></p>"""
)
pdf.output("link_PDF.pdf")