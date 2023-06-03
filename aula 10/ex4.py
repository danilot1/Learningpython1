while quantidade_notas > 0:
    nota = int(input('Digite uma nota: '))
    if nota % 2 != 0:
        continue
    soma = soma + nota
    quantidade_notas = quantidade_notas - 1 
print('Media:',soma/5)