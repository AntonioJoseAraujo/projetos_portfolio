from pikepdf import Pdf, Permissions, Encryption

with Pdf.open('demo.pdf') as pdf:
    restricoes = Permissions(extract=False,modify_form=False)
    pdf.save('demo_com_senha.pdf',encryption=Encryption(user='QWER!@#123', allow=restricoes))
    pdf.close()