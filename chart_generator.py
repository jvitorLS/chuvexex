import matplotlib
matplotlib.use('TkAgg')  # Configura o backend interativo
import matplotlib.pyplot as plt
import base64
import io

class ChuvexGraphGenerator:
    def __init__(self, data):
        """
        Inicializa a classe com os dados fornecidos.
        :param data: Lista de dicionários contendo informações sobre os bairros.
        """
        self.data = data

    def plot_population_line_graph(self):
        """
        Gera um gráfico de linha mostrando o bairro com o maior número de habitantes
        e o salva como uma string em base64.
        """
        bairros = [item['Bairro'] for item in self.data]
        habitantes = [item['Habitantes'] for item in self.data]

        # Criação do gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(bairros, habitantes, marker='o', label='Habitantes', color='b')
        plt.title('População por Bairro', fontsize=14)
        plt.xlabel('Bairro', fontsize=12)
        plt.ylabel('Número de Habitantes', fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(alpha=0.3)
        plt.legend()
        plt.tight_layout()

        # Salvar o gráfico em uma imagem em memória
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Codificar a imagem em base64
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # Fechar o gráfico para liberar memória
        buf.close()

        # Retornar o gráfico em base64
        return img_base64

    def plot_bairro_comparison(self, bairro_name):
        """
        Gera um gráfico de barras para o bairro especificado, mostrando número de habitantes, KM2 e altitude.
        :param bairro_name: Nome do bairro a ser analisado.
        """
        bairro = next((item for item in self.data if item['Bairro'] == bairro_name), None)
        if not bairro:
            print(f"Bairro '{bairro_name}' não encontrado nos dados.")
            return
        
        densidade_demografica = bairro['Habitantes'] / bairro['KM²']
        categorias = ['Habitantes','KM2']
        valores = [bairro['Habitantes'], bairro['KM²']]

        plt.figure(figsize=(8, 5))
        bars = plt.bar(categorias, valores, color=['blue', 'green'], alpha=0.8, width=0.5)


        for bar, valor in zip(bars, valores):
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_height() + 0.1,            
                f"{valor:.2f}",                    
                ha='center',
                fontsize=10
            )

        plt.title(
            f"Comparativo de Dados do Bairro: {bairro_name}\n\nDensidade Demográfica: {densidade_demografica:.2f} hab/km²", 
            fontsize=14
        )
        plt.ylabel('Valores', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        
        # Salvar o gráfico em uma imagem em memória
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Codificar a imagem em base64
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # Fechar o gráfico para liberar memória
        buf.close()

        # Retornar o gráfico em base64
        return img_base64