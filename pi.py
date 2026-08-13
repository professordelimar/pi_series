import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Valor de referência
PI_REF = math.pi

def casas_decimais_corretas(valor_aproximado, valor_referencia=PI_REF, max_casas=10):
    """
    Estima o número de casas decimais corretas a partir do erro absoluto.

    Observação:
    Como estamos usando math.pi como referência, o limite prático é cerca de 15 casas.
    """
    erro = abs(valor_aproximado - valor_referencia)

    if erro == 0:
        return max_casas

    casas = int(math.floor(-math.log10(erro)))

    if casas < 0:
        casas = 0

    if casas > max_casas:
        casas = max_casas

    return casas

# ============================================================
# Método 1: Série de Leibniz
# ============================================================
def pi_leibniz(n):
    soma = 0.0
    for k in range(n):
        soma += (-1)**k / (2*k + 1)
    return 4 * soma
# ============================================================
# Método 2: Série de Nilakantha
# ============================================================
def pi_nilakantha(n):
    pi = 3.0
    for k in range(1, n + 1):
        sinal = (-1)**(k + 1)
        denominador = (2*k) * (2*k + 1) * (2*k + 2)
        pi += sinal * 4 / denominador
    return pi
# ============================================================
# Método 3: Monte Carlo
# ============================================================
def pi_monte_carlo(n, semente=42):
    random.seed(semente)
    dentro = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            dentro += 1
    return 4 * dentro / n
# ============================================================
# Método 4: Fórmula de Machin com série do arctan
# ============================================================
def arctan_serie(x, n):
    soma = 0.0
    for k in range(n):
        soma += (-1)**k * x**(2*k + 1) / (2*k + 1)
    return soma
def pi_machin(n):
    """
    Fórmula de Machin:

    pi = 16 arctan(1/5) - 4 arctan(1/239)

    Aqui arctan é calculado por série.
    """
    return 16 * arctan_serie(1/5, n) - 4 * arctan_serie(1/239, n)
# ============================================================
# Método 5: Chudnovsky
# ============================================================
def pi_chudnovsky(n):
    """
    Fórmula de Chudnovsky em versão float.

    Observação:
    Em float, rapidamente chegamos no limite de precisão do Python,
    que é cerca de 15 a 16 casas decimais.
    """
    soma = 0.0
    for k in range(n):
        numerador = (-1)**k * math.factorial(6*k) * (13591409 + 545140134*k)
        denominador = math.factorial(3*k) * (math.factorial(k)**3) * (640320**(3*k))
        soma += numerador / denominador
    pi = 426880 * math.sqrt(10005) / soma
    return pi

# ============================================================
# Valores de N para cada método
# ============================================================
N_leibniz = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
N_nilakantha = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]
N_monte_carlo = [100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
N_machin = list(range(1, 21))
N_chudnovsky = list(range(1, 8))

# ============================================================
# Calculando aproximações
# ============================================================
resultados = {}
resultados["Leibniz"] = {
    "N": N_leibniz,
    "pi": [pi_leibniz(n) for n in N_leibniz]
}
resultados["Nilakantha"] = {
    "N": N_nilakantha,
    "pi": [pi_nilakantha(n) for n in N_nilakantha]
}
resultados["Monte Carlo"] = {
    "N": N_monte_carlo,
    "pi": [pi_monte_carlo(n) for n in N_monte_carlo]
}
resultados["Machin"] = {
    "N": N_machin,
    "pi": [pi_machin(n) for n in N_machin]
}
resultados["Chudnovsky"] = {
    "N": N_chudnovsky,
    "pi": [pi_chudnovsky(n) for n in N_chudnovsky]
}

# ============================================================
# Calculando casas decimais corretas
# ============================================================
for metodo in resultados:
    valores_pi = resultados[metodo]["pi"]
    casas = [
        casas_decimais_corretas(valor)
        for valor in valores_pi
    ]
    erros = [
        abs(valor - PI_REF)
        for valor in valores_pi
    ]
    resultados[metodo]["casas"] = casas
    resultados[metodo]["erro"] = erros
    
# ============================================================
# GRÁFICO 1: Convergência para pi
# ============================================================
plt.figure(figsize=(10, 6))
for metodo in resultados:
    N = resultados[metodo]["N"]
    valores_pi = resultados[metodo]["pi"]
    plt.plot(N, valores_pi, marker="o", label=metodo)
plt.axhline(PI_REF, linestyle="--", label="math.pi")
plt.xscale("log")
plt.xlabel("N")
plt.ylabel("Aproximação de pi")
plt.title("Convergência dos métodos para pi")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()