# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

num = []

for i in range(1, 6):
    InNum = int(input("INSIRA UM NUMERO AQUI "))
    if InNum % 2 == 0:
        num.append(InNum)
soma = sum(num)
print(num)
print(soma)