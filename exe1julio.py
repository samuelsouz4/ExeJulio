# -*- coding: utf-8 -*-
"""exe1julio



    https://colab.research.google.com/drive/1EM3YmNxLlT32U-axkq_YeyxA97eupW0s
"""

# Ler uma matriz M 5 x 5, calcular e escrever as seguintes somas


M = [[int(input(f"M[{i}][{j}]: ")) for j in range(5)] for i in range(5)]

linha_3 = sum(M[3])
coluna_2 = sum(M[i][2] for i in range(5))
diagonal_principal = sum(M[i][i] for i in range(5))
diagonal_secundaria = sum(M[i][4 - i] for i in range(5))
total = sum(sum(row) for row in M)

print("a) Linha 3:", linha_3)
print("b) Coluna 2:", coluna_2)
print("c) Diagonal Principal:", diagonal_principal)
print("d) Diagonal Secundária:", diagonal_secundaria)
print("e) Total:", total)

# Ler 2 matrizes, A 4 x 6 e B 4 x 6

A = [[int(input(f"A[{i}][{j}]: ")) for j in range(6)] for i in range(4)]
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(6)] for i in range(4)]

S = [[A[i][j] + B[i][j] for j in range(6)] for i in range(4)]
D = [[A[i][j] - B[i][j] for j in range(6)] for i in range(4)]

print("Matriz Soma (S):")
for row in S:
    print(row)

print("Matriz Diferença (D):")
for row in D:
    print(row)

# 33 Ler uma matriz A de 4 x 4, calcular e escrever as somas dos elementos marcados com X.
# Utilizar estruturas de repetição.

A = [[int(input(f"A[{i}][{j}]: ")) for j in range(4)] for i in range(4)]

# superior esquerda
soma_1 = sum(A[i][j] for i in range(2) for j in range(2))

# inferior direita
soma_2 = sum(A[i][j] for i in range(2, 4) for j in range(2, 4))

# Triângulo inferior esquerdo
soma_3 = sum(A[i][j] for i in range(4) for j in range(i+1))

# Triângulo superior direito
soma_4 = sum(A[i][j] for i in range(1, 4) for j in range(4 - i, 4))

print("Soma Região 1:", soma_1)
print("Soma Região 2:", soma_2)
print("Soma Região 3:", soma_3)
print("Soma Região 4:", soma_4)

# 34 Ler uma matriz D 5 x 5 (sem valores duplicados).
# e escrever uma mensagem indicando se o valor de X existe ou NÃO na matriz.

D = [[int(input(f"D[{i}][{j}]: ")) for j in range(5)] for i in range(5)]
X = int(input("Digite o número a buscar: "))

existe = any(X in row for row in D)
print("Existe na matriz." if existe else "Não existe na matriz.")

# 35 Ler uma matriz G 5 x 5 e criar 2 vetores SL e SC de 5 elementos que contenham
# respectivamente as somas das linhas e das colunas de G. Escrever os vetores criados.

G = [[int(input(f"G[{i}][{j}]: ")) for j in range(5)] for i in range(5)]

SL = [sum(G[i]) for i in range(5)]
SC = [sum(G[i][j] for i in range(5)) for j in range(5)]

print("Somas das Linhas:", SL)
print("Somas das Colunas:", SC)

# 36 Ler uma matriz A 12 x 13 e divida todos os 13 elementos de cada uma das 12 linhas de A
# pelo valor do maior elemento daquela linha. Escrever a matriz A modificada.

A = [[int(input(f"A[{i}][{j}]: ")) for j in range(13)] for i in range(12)]

for i in range(12):
    maior = max(A[i])
    A[i] = [round(x / maior, 2) for x in A[i]]

print("Matriz Normalizada:")
for row in A:
    print(row)

# 37 Ler um vetor G de 13 elementos que contenha o gabarito da loteria esportiva

# 38 Logo após, ler uma matriz 13 x 3 que contenha a aposta de um jogador.


gabarito = [int(input(f"Gabarito[{i}]: ")) for i in range(13)]
aposta = [[int(input(f"Aposta[{i}][{j}]: ")) for j in range(3)] for i in range(13)]

pontos = simples = duplas = triplas = 0

for i in range(13):
    num = sum(aposta[i])
    if aposta[i][gabarito[i] - 1] == 1:
        pontos += 1
    if num == 1:
        simples += 1
    elif num == 2:
        duplas += 1
    elif num == 3:
        triplas += 1

print("Pontos:", pontos)
print("Simples:", simples)
print("Duplas:", duplas)
print("Triplas:", triplas)

# 39 Crie uma rotina de calculadora com funções básicas.
# 40 Multiplicação deve ser feita utilizando somas sucessivas.

def soma(a, b): return a + b
def sub(a, b): return a - b
def div(a, b): return a / b if b != 0 else "Divisão por zero"
def mult(a, b): return sum(a for _ in range(b))

a = int(input("1º valor: "))
b = int(input("2º valor: "))
op = input("Operação (+ - * /): ")

if op == '+':
    print("Resultado:", soma(a, b))
elif op == '-':
    print("Resultado:", sub(a, b))
elif op == '*':
    print("Resultado:", mult(a, b))
elif op == '/':
    print("Resultado:", div(a, b))

# 41 Função velocidade_media(distância, tempo).
# 42 Criar função divisao() e usar na velocidade_media().

def divisao(a, b): return a / b
def velocidade_media(distancia, tempo): return divisao(distancia, tempo)

d = float(input("Distância (m): "))
t = float(input("Tempo (s): "))
print("Velocidade Média:", velocidade_media(d, t), "m/s")

# 43 Organiza número. Faça uma rotina que organize os números recebidos.


def organiza(numero):
    numero = str(numero)
    crescente = ''.join(sorted(numero))
    decrescente = ''.join(sorted(numero, reverse=True))
    reverso = numero[::-1]
    return crescente, decrescente, reverso

n = input("Número: ")
c, d, r = organiza(n)
print("Crescente:", c)
print("Decrescente:", d)
print("Reverso:", r)

# 44 Conversão de horário 24h para 12h com função para conversão e saída.
def converter_hora(h, m):

# 45 Data com mês por extenso. Construa uma função que receba uma data no formato


def data_extenso(data):
    meses = [
        "", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    try:
        d, m, a = map(int, data.split("/"))
        if 1 <= m <= 12 and 1 <= d <= 31 and a > 0:
            return f"{d} de {meses[m]} de {a}"
        else:
            return None
    except:
        return None

# Exemplo de uso
entrada = input("Digite uma data no formato DD/MM/AAAA: ")
resultado = data_extenso(entrada)
if resultado is None:
    print("Data inválida")
else:
    print(resultado)
