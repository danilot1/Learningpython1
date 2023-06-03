pedido = int(input("Digite a quantidade de maca"))
maca = 0.30
if pedido > 15:
    maca = 0.25
    quantidade = pedido * maca 
    print("valor = ", quantidade) 
else:
    quantidade = pedido * 0.30
    print("Valor = ", quantidade)