## Primeira e última ocorrência de uma string
nome = str(input('Digite seu nome:')).upper().strip()
cont = nome.count('A')
conta = nome.find('A')
con = nome.rfind('A')
print('O nome tem {} no total,\nO primeiro A aparece na {} posição, \nO ultimo A aparece na {} posição'.format(cont, conta, con))