def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

print("-" * 30)
print("     CALCULADORA")
print("-" * 30)

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("0 - Sair")

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
operacao = input("Escolha a operação: ")

match operacao:
    case "1":
        print(f"Resultado: {somar(numero1, numero2):.2f}")
    case "2":
        print(f"Resultado: {subtrair(numero1, numero2):.2f}")
    case "3":
        print(f"Resultado: {multiplicar(numero1, numero2):.2f}")
    case "4":
        if numero2 == 0:
            print("Erro: divisão por zero.")
        else:
            print(f"Resultado: {dividir(numero1, numero2):.2f}")
    case "0":
        print("Até logo!")
    case _:
        print("Opção inválida.")
