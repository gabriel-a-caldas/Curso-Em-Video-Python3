# Faça um algoritmo que leia um número e diga
# seu antecessor e seu sucessor

numero1 = int(input("Insira um número: "))

sucessor = numero1+1
antecessor = numero1-1

print(f' {antecessor} < {numero1} < {sucessor}')