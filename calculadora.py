def soma():
    valor1 = float(input("Digite um numero:"));
    valor2 = float(input("Digite outro numero:"));
    resultS = valor1 + valor2
    return resultS

def subtracao():
    valor1 = float(input("Digite um numero:"));
    valor2 = float(input("Digite outro numero:"));
    resultSu = valor1 - valor2
    return resultSu

def multiplicacao():
    valor1 = float(input("Digite um numero:"));
    valor2 = float(input("Digite outro numero:"));
    resultM = valor1 * valor2
    return resultM

def divisao():
    valor1 = float(input("Digite um numero:"));
    valor2 = float(input("Digite outro numero:"));
    resultD = valor1 / valor2
    if valor2 == 0:
        return "Erro: Divisão por zero"
    return resultD

def default():
    return "Opção inválida."

switch ={
        "+": soma,
        "-": subtracao,
        "*": multiplicacao,
        "/": divisao
}

opção = (input("Digite um operador(+, -, *, /):"))

resultado = switch.get(opção, default)()

print(f"Seu resultado:{resultado}")


