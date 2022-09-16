"""
print(1, 68, 25, 35)

print(type(1))

print(type(68))

print(type(25))

print(type(35))

print((-1), (-68), 25, 35)
print(type(-68))



print(1.8, 23.5, -350.9, 1.0)
print(type(1.8))


print(True, False)


print("voce e" + 3* " Muito" + " Legal!!!")

print('voce e' + 3* ' Muito' + ' Legal!!!')

print("Assim 'pode', vai dar certo")
print("Assim \"pode\", vai dar certo, \npara pular linha, dar \tespaco maior")


lista = ([1, 2, 3])

print(lista)


qualquer = ({'nome': 'Daniel', 'idade': '25'})

print(qualquer)

print(None)

a = 2
b = 35
c = "Ola, sou uma variavel que varia!!!"

a = 9

c = '8'
#print(a + c)

print(f"Ola : {a}")
"""
"""
print(3 > 7)
print(4>=6)
print(4<6)
print(4<=6)
print(5!=6)
print(5!=5)
print(5 ==5 )
print(2 == '2')



# Opereadores de atribuição


simples = "String"
a = 3 
b = a 

#a = a + 7
a += 7
print(a)
a -= 7
print(a)
a *= 7
print(a)
a /= 7
print(a)
a %= 7
print(a)
a **= 7
print(a)
a //= 7
print(a)

print(True)
print(False)

7!=3 and 2 > 3

# Tabela Verdade AND (&)
print(True and True) 
print(True and False) 
print(False and True) 
print(False and False)
print(True and True and True and False and True) 


# Ou - Or

print(True or True)
print(False or True)
print(True or False)
print(False or False)
print(False or False or False or False or True or False)


#Xor- OU Exclusivo

print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Operador Unário de Negação


print(not True)
print(not False)

saldo = 1000
salario = 4000
despesas = 968

saldo_positivo =  saldo > 0
percentual_despesas = despesas >= 0.2 * salario

meta = saldo_positivo and percentual_despesas

print(f'O resultado da meta foi {meta}')






    -Confirmado os 2: Tv 50' + sorvete
    -Confirmado Apenas 1: Tv 32' + sorvete
    -Nenhum confirmado: Fica em casa



trabalho_terca = True
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saudavel = not sorvete

print("Tv50= {} Tv32= {} Sorvete= {} Saudavel= {}" .format(tv_50, tv_32, sorvete, mais_saudavel))






esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas' , 'molhadas') [esta_chovendo])

esta_chovendo = False
print('Hoje estou com roupas ' + ('molhadas' if esta_chovendo else 'secas'))




lista = [1,2,3, "Paulo", "José"]
print(2 in lista)
print("Paulo" in lista)
print("Joao" in lista)
print("José" not in lista)




print("Ola estou com \"aspas\" duplas")
print('Ola estou com "aspas" duplas')



x = 3

y = x 

z = 3

print(x is y)
print(y is z)
print(y is not z)



lista_x = [1,2,3]
lista_y = lista_x
lista_z = [1,2,3]

lista_x[2] = 300
lista_z[2] = 300
lista_z[0] = 50



print(__builtins__.type("ola"))

#print(dir(__builtins__))

print(2+3)
print(int('2')+int('3'))




a = 2
b = '3'

print(a + int(b))


#print(2 +int('2 qualquer'))


print(20/2)

print(10//3)
print(10//3.3)


#print(dir(int))


#print(dir(int))
#print(dir(float))

a = 5
b = 2.5

print(type(a))
print(b.is_integer())
print(int.__pow__(2,3))
print(2**3)

print((-2).__abs__())
print(abs(-2))

help(float)





print(1.1 + 2.2)

from decimal import Decimal, getcontext

print(1/7)
print(Decimal(1)/(7))

getcontext().prec = 2
print(Decimal(1.1) + Decimal(2.2))

#print(dir(Decimal))



from ntpath import join


nome = 'Daniel Adorno'
print(nome[1])

#nome[0] = 'P'
print(nome)

doc = Ola eu sou um texto
         com Multiplas..... 
        .....linhas
print(doc)   


print(nome[4:])
print(nome[:3])
print(nome[2:5])

numeros = '1234567890'

print(numeros[::])
print(numeros[::-1])
print(numeros[::-2])
print(numeros[1::2])
print(nome[::-1])

frase = 'A vida e bela, viva com sabedoria!!!!'


print('v' in frase)

frase = frase.upper()
print(frase)
#print(len(frase))
frase = frase.lower()
print(frase)

help(str)

texto = ('ab', 'cd', 'df')

novotexto = " ".join(texto)

print(novotexto)

"""


""" lista = []
print(type(lista))
#print(dir(lista))

lista= ['Daniel', 'Gabriel', 'Miguel', 'Emanuel', 123, 963, 28]

print(lista[-5])

tupla = tuple()
print(type(tupla)) """

#print(dir(tupla))


""" pessoa = {'nome': 'Daniel', 'idade': 26, 'curso': ['Python Basico', 'Praticas de Androd']}

#print(dir(dict))

pessoa['idade'] = 25
print(pessoa.keys())
print(pessoa.values())
print(pessoa.__len__())

print(pessoa.items())
 
print(pessoa.pop('idade'))
print(pessoa.items())

pessoa.update({'Idade': 26, 'Sexo': 'Maculino'})

print(pessoa.items()) """



 
# ConJuntos


a = {1,2,3}
print(type(a))


c = {'A': 1, 'B': 2, 'C': 3}




b = set('Escola')

print(b)
print('E' in b, 'F' not in b)




print({1,2,3} == {3,2,1,3})






c1 = {1,2}
c2 = {2,3}

print(c1.union(c2))

c1.update(c2)

print(c1)
print(c2 <= c1)
print(c1 >= c2)

print(c1-c2)



#INTERPOLAÇÂO

from string import Template

nome, idade = 'Daniel', 26.78789
print('Nome: %s Idade: %.2f' % (nome, idade))



print('Nome: {0} Idade: {1}' .format(nome, idade))

print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))





# RAIO 15.3
# Pi = 3.14159








