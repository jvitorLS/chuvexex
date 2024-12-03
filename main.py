import os
import base64
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from pdfkit import from_string
from chart_generator import ChuvexGraphGenerator
from data_handler import CSVReader
from pychromepdf import ChromePDF
from template import gerar_html

# Função principal (main) - Executa as classes
PATH_TO_CHROME_EXE = '/usr/bin/firefox'

def main():
    # Configuração do ambiente e caminho do arquivo CSV
    csv_path = os.path.join(os.path.dirname(__file__), 'dados.csv')

    # Solicitar do usuário o nome do bairro
    bairro_input = input("Digite o nome do bairro para gerar os gráficos: ")
    
    # 1. Carregar e analisar dados com a classe CSVReader
    reader = CSVReader(csv_path)
    data = reader.load_data()

    # 2. Criar gráfico com a classe ChuvexGraphGenerator
    chuvex = ChuvexGraphGenerator(data.to_dict('records'))

    # Gerando o gráfico de linha para número de habitantes e obtendo o base64
    print("Gerando gráfico de linha para população por bairro...")
    population_graph_base64 = chuvex.plot_population_line_graph()

    # Gerando o gráfico de barras para um bairro específico e obtendo o base64
    print(f"Gerando gráfico de barras para o bairro: {bairro_input}...")
    bairro_comparison_graph_base64 = chuvex.plot_bairro_comparison(bairro_input)

    # Salvar o HTML para visualização (ou processamento posterior)
    html = gerar_html(bairro_input, population_graph_base64, bairro_comparison_graph_base64)

    pdf_output_path = os.path.join(os.path.dirname(__file__), 'output.pdf')

    # Abrir o arquivo de saída PDF para escrita
    with open(pdf_output_path, 'wb') as output_file:
        cpdf = ChromePDF(PATH_TO_CHROME_EXE)
        if cpdf.html_to_pdf(html, output_file):
            print(f"PDF gerado e salvo como {pdf_output_path}.")
        else:
            print("Erro ao gerar o PDF.")

if __name__ == "__main__":
    main()