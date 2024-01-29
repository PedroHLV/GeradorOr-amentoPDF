from fpdf import FPDF

# Projeção futura: Criar um executavel com uma interface gráfica para esse código para enviar para o cliente preencher

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")
valor_total_estimado = int(horas_estimadas) * int(valor_hora)

# Criando PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

# Inserindo dados no PDF
pdf.image("./templates/img/template.png", x=0, y=0) # Substituir pelo meu template personalizado.
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total_estimado))

# Salvando o arquivo
pdf.output("Orçamento.pdf")
print("PDF gerado com sucesso.")