hora = int(input())

if  hora<6:
    print("É madrugada")
elif hora < 12:
    print("Bom dia")
elif hora <18:
    print("Boa tarde")
elif hora <=24:
    print("Boa noite")
else:
    print('Horario invalido')