print("Testando as Variáveis em Python\n")
salario = 2500
aumento = salario * 25 / 100
novoSalario = salario + aumento
print("O novo salário é R$", novoSalario)

print("\nProximo exemplo 2", "f(x) = x² + 1")
def f(x):
    res = x**2 + 1
    return res
print(f(4))

#
print("\nProximo exemplo 4 -", "Função que calcula o preço de um produto atualizado pela taxa de juros:")
def juros(preco,juros):
    res = preco * (1 + (juros / 100))
    return res
print(juros(10, 50))

#preço=10 e juros=50

print("\nExemplo 5 - Variáveis")
nome=input("Digite o seu nome: ")
areaCurso=input("Digite a área de seu curso em maiúscula: ")
print("O meu nome é ", nome, "e o meu curso é da área de -", areaCurso,"- UNIVESP")
