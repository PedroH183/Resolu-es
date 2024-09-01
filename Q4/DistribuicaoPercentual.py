
faturamento_mensal = {
    "SP"  : "67.836,43",
    "RJ"  : "36.678,66",
    "MG"  : "29.229,88",
    "ES"  : "27.165,48",
    "Outros" : "19.849,53"
}

class FaturamentoMensal:

    faturamento_float = {}

    def __init__(self, faturamento_mensal):

        for estado, valor in faturamento_mensal.items():
            valor_float = float(valor.replace('.', '').replace(',', '.'))
            self.faturamento_float[estado] = valor_float

    def representacao_percentual(self):
        total_faturamento = sum(self.faturamento_float.values())

        percentual_representation = {}

        for estado, faturamento in self.faturamento_float.items():
            percentual = (faturamento / total_faturamento) * 100
            percentual_representation[estado] = percentual

        return percentual_representation


manager = FaturamentoMensal(faturamento_mensal)
percentuais = manager.representacao_percentual()

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")