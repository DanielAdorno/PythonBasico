

sexo = str(input('Informe o sexo: [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, por favor Digite um sexo Válido: [M/F]: ')).strip().upper()[0]

print('Dado registrado com Sucesso!!!')
