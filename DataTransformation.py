import camelot
import pandas as pd
import zipfile
import time

#ler as páginas especificas do PDF
tables = camelot.read_pdf("Padrão_TISS_Componente_Organizacional_202103.pdf", pages='79-85')
tabela = tables[0]
#imprimir tabelas
for tabela in tables:
    print(tabela.df)

#exportar para csv
tabela.to_csv('tabelas.csv')

#esperar 5 segundos
time.sleep(5)

#comprimindo o arquivo csv criado
zf = zipfile.ZipFile('Teste_Intuitive_Care_Jonathan_Henrique.zip')
zf.write("tabelas.csv")
zf.close()    