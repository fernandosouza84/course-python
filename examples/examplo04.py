#Programa de media ponderada
print('----------------------------------------------')
print('Media ponderada')
peso1 = float(input('Digite o peso da primeira prova: '))
peso2 = float(input('Digite o peso da segunda prova: '))
nota1 = float(input('Digite a nota primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
result1 = peso1 * nota1;
result2 = peso2 * nota2;
media = (result1 + result2) / (peso1 + peso2)

print('A soma dos valores é: ', media)
print('---------------------------------------------')
