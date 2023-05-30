import fpdf
from fpdf import FPDF

produto1 = input("Descrição do Produto 1: ")
produto2 = input("Descrição do Produto 2: ")
produto3 = input("Descrição do Produto 3: ")

preçoProduto_1 = int(input("Preço do Produto 1: "))
preçoProduto_2 = int(input("Preço do Produto 2: "))
preçoProduto_3 = int(input("Preço do Produto 3: "))

qtdProduto_1 = int(input("Quantidade do Produto 1: "))
qtdProduto_2 = int(input("Quantidade do Produto 2: "))
qtdProduto_3 = int(input("Quantidade do Produto 3: "))

totalProduto_1 = preçoProduto_1 * qtdProduto_1
totalProduto_2 = preçoProduto_2 * qtdProduto_2
totalProduto_3 = preçoProduto_3 * qtdProduto_3

preçoTotal = totalProduto_1 + totalProduto_2 + totalProduto_3

cifrao = "$"

print(preçoTotal)

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", "B", 12)

pdf.set_text_color(0, 0, 0)

pdf.image("template_modelo.png", x=0, y=0)

pdf.text(50, 160, produto1)
pdf.text(50, 182, produto2)
pdf.text(50, 205, produto3)

pdf.text(130, 160, cifrao+str(preçoProduto_1))
pdf.text(130, 182, cifrao+str(preçoProduto_2))
pdf.text(130, 205, cifrao+str(preçoProduto_3))

pdf.text(150, 160, str(qtdProduto_1))
pdf.text(150, 182, str(qtdProduto_2))
pdf.text(150, 205, str(qtdProduto_3))

pdf.text(170, 160, cifrao+str(totalProduto_1))
pdf.text(170, 182, cifrao+str(totalProduto_2))
pdf.text(170, 205, cifrao+str(totalProduto_3))

pdf.set_text_color(255, 255, 255)
pdf.set_font("Arial", "B", 14)


pdf.text(170, 220, cifrao+str(preçoTotal))

pdf.output("orçamento-gerado.pdf")
