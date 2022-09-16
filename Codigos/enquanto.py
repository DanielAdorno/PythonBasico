# Laços de repetições Enqunto



# numero = 0

# while numero <= 10:
#     print(numero)
#     numero += 1
# print("Fim")






# resposta = 'S'
# while resposta == 'S':
#     numero_aleatorio = int(input('Digite um número qualquer: '))
#     resposta = str(input('Quer continuar digitando? [S/N]')).upper()
# print('Fim do programa!!!!')







numero = 1
par = impar = 0
while numero !=0:
    numero = int(input('Digite um número: '))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')          





"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""



