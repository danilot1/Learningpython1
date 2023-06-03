idade = int(input())

if idade < 12:
  print('o usuário é criança')
elif idade < 18:
  print('o usuário é adolescente')
elif idade < 32:
  print('o usuário é jovem')
elif idade < 60:
  print('o usuário é adulto')
else:
  print('o usuário é idoso')
