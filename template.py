import os

# Função para gerar o HTML e salvar em um arquivo
def gerar_html(bairro_input, population_graph_base64, bairro_comparison_graph_base64):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gráficos Gerados Chuvex</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            .image-container {{
                margin-bottom: 20px;
                text-align: center;
            }}
            .image-container img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Gráficos Gerados Chuvex</h1>
        <div class="image-container">
            <img src="data:image/png;base64,{population_graph_base64}" alt="Gráfico de População por Bairro">
        </div>
        <div class="image-container">
            <img src="data:image/png;base64,{bairro_comparison_graph_base64}" alt="Comparativo de Dados do Bairro: ">
        </div>
    </body>
    </html>
    """

    # Salvar HTML em arquivo
    html_output_path = 'output.html'
    with open(html_output_path, 'w') as f:
        f.write(html_content)
    print("HTML gerado e salvo como output.html.")
    
    return html_output_path
