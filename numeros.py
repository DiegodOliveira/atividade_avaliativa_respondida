# Questão 3 da atividade avaliativa

op = str(input("Qual o tipo de operação que você quer fazer?"))
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))

ad = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
expo = n1 ** n2

if op == "subtração":
    print(sub)
elif op == "adição":
    print(ad)
elif op == "multiplicação":
    print(mult)
elif op == "divisão":
    print(div)
elif op == "exponenciação":
    print(expo)
else:
    print("Digite o nome de uma operação válida!")