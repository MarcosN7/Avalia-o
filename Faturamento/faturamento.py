import json

with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

faturamento = [float(valor) for valor in faturamento.values()]

dias = len(faturamento)
soma = sum(faturamento)
media = soma / dias
maior = max(faturamento)
menor = min(faturamento)
acima_da_media = sum(1 for x in faturamento if x > media)

print("Menor faturamento diário:", menor)
print("Maior faturamento diário:", maior)
print("Dias acima da média mensal:", acima_da_media)
