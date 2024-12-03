import pandas as pd

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Carrega os dados do CSV e prepara para uso.
        """
        # Leitura do CSV
        self.data = pd.read_csv(self.file_path)
        
        # Convertendo colunas numéricas para os tipos apropriados
        self.data['Habitantes'] = self.data['Habitantes'].astype(int)
        self.data['KM²'] = self.data['KM²'].astype(float)
        self.data['Altitude'] = self.data['Altitude'].astype(int)
        
        print("Dados carregados e preparados:")
        print(self.data.head())  # Exibe as primeiras linhas para validação
        return self.data
