name1 = input()
data_de_nascimento1 = input()
name2 = input()
data_de_nascimento2 = input()

if data_de_nascimento1 < data_de_nascimento2:
    print(name1, 'é mais velho que ',name2)
elif data_de_nascimento1 > data_de_nascimento2:
    print(name2, 'é mais velho que ',name1)