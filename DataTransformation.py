import zipfile
import io
import PyPDF2
import tabula
import pandas as pd

# Abrir o arquivo PDF
with open("Padrão_TISS_Componente_Organizacional_202103.pdf", "rb") as f:
    # Criar um objeto PDFReader para ler o arquivo
    reader = PyPDF2.PdfFileReader(f)

    # Iterar sobre as páginas do arquivo
    for i in range(79, 86):
        # Extrair o texto da página
        page = reader.getPage(i-1)
        text = page.extractText()

        # Usar o módulo tabula para extrair tabelas do texto da página
        df = tabula.read_pdf(io.StringIO(text), pages='all')

        # Escrever o dataframe em um arquivo CSV
        df.to_csv(f'tabela_{i}.csv', index=False)

# Cria um objeto ZipFile com o nome do arquivo ZIP desejado
zip_file = zipfile.ZipFile("tabelas.zip", mode="a")

# Adiciona o arquivo CSV ao arquivo ZIP
for i in range(79, 86):
    zip_file.write(f"tabela_{i}.csv")

# Adiciona os demais arquivos CSV aqui

# Fecha o arquivo ZIP
zip_file.close()
