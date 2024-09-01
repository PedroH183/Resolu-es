import json

class DistribuicaoManager:
    def __init__(self, json_file_path):
        self.faturamento_diario = self.load_faturamento_from_json(json_file_path)

    def load_faturamento_from_json(self, json_file_path):
        # carregamento do arquivo de entrada.
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return [dia['faturamento'] for dia in data['faturamento_diario'] if dia['faturamento'] > 0]

    def menor_faturamento(self):
        return min(self.faturamento_diario)

    def maior_faturamento(self):
        return max(self.faturamento_diario)

    def faturamento_mensal_medio(self):
        return sum(self.faturamento_diario) / len(self.faturamento_diario)

    def qtd_dias_faturamento_menor_que_mensal(self):
        media_mensal = self.faturamento_mensal_medio()
        return sum(1 for faturamento in self.faturamento_diario if faturamento < media_mensal)


if __name__ == "__main__":
    manager = DistribuicaoManager('faturamento_diario.json')

    print("Menor Faturamento:", manager.menor_faturamento())
    print("Maior Faturamento:", manager.maior_faturamento())
    print("Faturamento Médio Mensal:", manager.faturamento_mensal_medio())
    print("Quantidade de Dias com Faturamento Menor que a Média Mensal:", manager.qtd_dias_faturamento_menor_que_mensal())