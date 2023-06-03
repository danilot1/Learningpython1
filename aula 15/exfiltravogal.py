def filtravogais(palavra):
    for i in palavra:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            print(i)
    
palavra = input()
palavra = filtravogais(palavra)
print(palavra)

