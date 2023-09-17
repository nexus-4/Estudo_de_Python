import PyPDF2

# Caminho para o arquivo PDF de entrada e saída
arquivo_entrada = 'Callioli5.pdf'
arquivo_saida = 'Callioli6.pdf'

# Abrir o arquivo PDF de entrada no modo de leitura binária
with open(arquivo_entrada, 'rb') as pdf_entrada:
    # Criar um objeto PdfReader para ler o PDF
    pdf_reader = PyPDF2.PdfReader(pdf_entrada)

    # Criar um objeto PdfFileWriter para escrever o PDF corrigido
    pdf_writer = PyPDF2.PdfWriter()

    # Iterar através de cada página e girar 90 graus no sentido horário
    for pagina_num in range(len(pdf_reader.pages)):
        pagina = pdf_reader.pages[pagina_num]
        pagina.rotate(90)
        pdf_writer.add_page(pagina)

    # Abrir o arquivo PDF de saída no modo de escrita binária
    with open(arquivo_saida, 'wb') as pdf_saida:
        # Salvar o PDF corrigido no arquivo de saída
        pdf_writer.write(pdf_saida)

print(f'O PDF foi corrigido e salvo como "{arquivo_saida}".')
