# ============================================================
# PROJETO: APROXIMACOES DO NUMERO PI COM PYTHON
# Versao didatica para estudantes do Ensino Medio/Tecnico
# ============================================================

import math
import random
import numpy as np
import matplotlib.pyplot as plt

try:
    from scipy.interpolate import interp1d
    SCIPY_DISPONIVEL = True
except ImportError:
    SCIPY_DISPONIVEL = False


# ============================================================
# CONFIGURACOES GERAIS
# ============================================================

PI_REF = math.pi

# Mesmo limite inicial e final do eixo x para todos os metodos
X_MIN = 1
X_MAX = 1_000_000

# Mesmo limite do eixo y para facilitar comparacao visual
Y_MIN = 3.10
Y_MAX = 3.18
Y_PASSO = 0.01

# Pasta/nomes das figuras: as figuras serao salvas na mesma pasta do script
DPI_FIGURA = 300


# ============================================================
# FUNCOES MATEMATICAS PARA APROXIMAR PI
# ============================================================

# ============================================================
# Metodo 1: Serie de Leibniz
# ============================================================
def pi_leibniz(n):
    soma = 0.0

    for k in range(n):
        soma += (-1)**k / (2*k + 1)

    return 4 * soma


# ============================================================
# Metodo 2: Serie de Nilakantha
# ============================================================
def pi_nilakantha(n):
    pi = 3.0

    for k in range(1, n + 1):
        sinal = (-1)**(k + 1)
        denominador = (2*k) * (2*k + 1) * (2*k + 2)
        pi += sinal * 4 / denominador

    return pi


# ============================================================
# Metodo 3: Monte Carlo
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
# Metodo 4: Formula de Machin com serie do arctan
# ============================================================
def arctan_serie(x, n):
    soma = 0.0

    for k in range(n):
        soma += (-1)**k * x**(2*k + 1) / (2*k + 1)

    return soma


def pi_machin(n):
    return 16 * arctan_serie(1/5, n) - 4 * arctan_serie(1/239, n)


# ============================================================
# Metodo 5: Chudnovsky
# ============================================================
def pi_chudnovsky(n):
    soma = 0.0

    for k in range(n):
        numerador = (-1)**k * math.factorial(6*k) * (13591409 + 545140134*k)
        denominador = math.factorial(3*k) * (math.factorial(k)**3) * (640320**(3*k))
        soma += numerador / denominador

    pi = 426880 * math.sqrt(10005) / soma

    return pi


# ============================================================
# FUNCOES AUXILIARES PARA GRAFICOS
# ============================================================

def configurar_grafico_padrao():
    plt.xscale("log")
    plt.xlim(X_MIN, X_MAX)
    plt.ylim(Y_MIN, Y_MAX)
    plt.yticks(np.arange(Y_MIN, Y_MAX + Y_PASSO, Y_PASSO))
    plt.xlabel("N")
    plt.ylabel("Aproximacao de pi")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()


def salvar_figura(nome_arquivo):
    plt.savefig(nome_arquivo, dpi=DPI_FIGURA, bbox_inches="tight")
    plt.show()


def interpolar_curva(N_original, pi_original, N_novo):
    """
    Interpola visualmente os valores de pi em funcao de log10(N).

    A interpolacao e usada apenas para suavizar as curvas nos graficos.
    Os pontos originais continuam sendo os valores efetivamente calculados.
    """

    N_original = np.asarray(N_original, dtype=float)
    pi_original = np.asarray(pi_original, dtype=float)

    ordem = np.argsort(N_original)
    N_original = N_original[ordem]
    pi_original = pi_original[ordem]

    logN_original = np.log10(N_original)
    logN_novo = np.log10(N_novo)

    if SCIPY_DISPONIVEL:
        f = interp1d(
            logN_original,
            pi_original,
            kind="linear",
            bounds_error=False,
            fill_value=(pi_original[0], pi_original[-1])
        )
        return f(logN_novo)

    return np.interp(
        logN_novo,
        logN_original,
        pi_original,
        left=pi_original[0],
        right=pi_original[-1]
    )


# ============================================================
# ENTRADAS DE CADA METODO
# ============================================================
# Os metodos possuem entradas diferentes porque convergem em velocidades diferentes.
# Mesmo assim, todos os graficos usam o mesmo limite visual de x: 1 ate 1.000.000.

N_leibniz = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
N_nilakantha = [1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
N_monte_carlo = [100, 300, 1000, 3000, 10000, 30000, 100000, 300000, 1000000]
N_machin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N_chudnovsky = [1, 2, 3, 4, 5, 6, 7]


# ============================================================
# EXECUCAO SEPARADA DE CADA METODO
# ============================================================

# Leibniz
pi_leibniz_resultados = [pi_leibniz(n) for n in N_leibniz]

# Nilakantha
pi_nilakantha_resultados = [pi_nilakantha(n) for n in N_nilakantha]

# Monte Carlo
pi_monte_carlo_resultados = [pi_monte_carlo(n) for n in N_monte_carlo]

# Machin
pi_machin_resultados = [pi_machin(n) for n in N_machin]

# Chudnovsky
pi_chudnovsky_resultados = [pi_chudnovsky(n) for n in N_chudnovsky]


# ============================================================
# IMPRESSAO DIDATICA DOS RESULTADOS
# ============================================================

print("Valor de referencia de pi:", PI_REF)
print()

print("Metodo de Leibniz")
for n, valor in zip(N_leibniz, pi_leibniz_resultados):
    print(f"N = {n:<10} pi = {valor:.15f}")
print()

print("Metodo de Nilakantha")
for n, valor in zip(N_nilakantha, pi_nilakantha_resultados):
    print(f"N = {n:<10} pi = {valor:.15f}")
print()

print("Metodo de Monte Carlo")
for n, valor in zip(N_monte_carlo, pi_monte_carlo_resultados):
    print(f"N = {n:<10} pi = {valor:.15f}")
print()

print("Metodo de Machin")
for n, valor in zip(N_machin, pi_machin_resultados):
    print(f"N = {n:<10} pi = {valor:.15f}")
print()

print("Metodo de Chudnovsky")
for n, valor in zip(N_chudnovsky, pi_chudnovsky_resultados):
    print(f"N = {n:<10} pi = {valor:.15f}")
print()


# ============================================================
# GRAFICO 1: CONVERGENCIA GERAL, SEM LOOP NA PLOTAGEM
# ============================================================

plt.figure(figsize=(11, 7))

plt.plot(N_leibniz, pi_leibniz_resultados, marker="o", linewidth=2, label="Leibniz")
plt.plot(N_nilakantha, pi_nilakantha_resultados, marker="o", linewidth=2, label="Nilakantha")
plt.plot(N_monte_carlo, pi_monte_carlo_resultados, marker="o", linewidth=2, label="Monte Carlo")
plt.plot(N_machin, pi_machin_resultados, marker="o", linewidth=2, label="Machin")
plt.plot(N_chudnovsky, pi_chudnovsky_resultados, marker="o", linewidth=2, label="Chudnovsky")

plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")

configurar_grafico_padrao()
salvar_figura("figura_01_convergencia_geral.png")


# ============================================================
# GRAFICO 2: LEIBNIZ
# ============================================================

plt.figure(figsize=(10, 6))
plt.plot(N_leibniz, pi_leibniz_resultados, marker="o", linewidth=2, label="Leibniz")
plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")
configurar_grafico_padrao()
salvar_figura("figura_02_leibniz.png")


# ============================================================
# GRAFICO 3: NILAKANTHA
# ============================================================

plt.figure(figsize=(10, 6))
plt.plot(N_nilakantha, pi_nilakantha_resultados, marker="o", linewidth=2, label="Nilakantha")
plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")
configurar_grafico_padrao()
salvar_figura("figura_03_nilakantha.png")


# ============================================================
# GRAFICO 4: MONTE CARLO
# ============================================================

plt.figure(figsize=(10, 6))
plt.plot(N_monte_carlo, pi_monte_carlo_resultados, marker="o", linewidth=2, label="Monte Carlo")
plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")
configurar_grafico_padrao()
salvar_figura("figura_04_monte_carlo.png")


# ============================================================
# GRAFICO 5: MACHIN
# ============================================================

plt.figure(figsize=(10, 6))
plt.plot(N_machin, pi_machin_resultados, marker="o", linewidth=2, label="Machin")
plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")
configurar_grafico_padrao()
salvar_figura("figura_05_machin.png")


# ============================================================
# GRAFICO 6: CHUDNOVSKY
# ============================================================

plt.figure(figsize=(10, 6))
plt.plot(N_chudnovsky, pi_chudnovsky_resultados, marker="o", linewidth=2, label="Chudnovsky")
plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")
configurar_grafico_padrao()
salvar_figura("figura_06_chudnovsky.png")


# ============================================================
# CURVAS DE CONVERGENCIA SUAVIZADAS
# ============================================================
# Nao e necessario indicar no grafico que as curvas foram interpoladas.

N_suave = np.logspace(np.log10(X_MIN), np.log10(X_MAX), 1000)

pi_leibniz_suave = interpolar_curva(N_leibniz, pi_leibniz_resultados, N_suave)
pi_nilakantha_suave = interpolar_curva(N_nilakantha, pi_nilakantha_resultados, N_suave)
pi_monte_carlo_suave = interpolar_curva(N_monte_carlo, pi_monte_carlo_resultados, N_suave)
pi_machin_suave = interpolar_curva(N_machin, pi_machin_resultados, N_suave)
pi_chudnovsky_suave = interpolar_curva(N_chudnovsky, pi_chudnovsky_resultados, N_suave)


# ============================================================
# GRAFICO 7: TODAS AS CURVAS SUAVIZADAS
# ============================================================

plt.figure(figsize=(11, 7))

plt.plot(N_suave, pi_leibniz_suave, linewidth=2.5, label="Leibniz")
plt.plot(N_suave, pi_nilakantha_suave, linewidth=2.5, label="Nilakantha")
plt.plot(N_suave, pi_monte_carlo_suave, linewidth=2.5, label="Monte Carlo")
plt.plot(N_suave, pi_machin_suave, linewidth=2.5, label="Machin")
plt.plot(N_suave, pi_chudnovsky_suave, linewidth=2.5, label="Chudnovsky")

plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")

configurar_grafico_padrao()
salvar_figura("figura_07_curvas_suavizadas.png")


# ============================================================
# GRAFICO 8: CURVAS SUAVIZADAS COM PONTOS CALCULADOS
# ============================================================
# Esta figura e recomendada para o artigo porque mostra as curvas e os pontos.

plt.figure(figsize=(11, 7))

plt.plot(N_suave, pi_leibniz_suave, linewidth=2.5, label="Leibniz")
plt.plot(N_suave, pi_nilakantha_suave, linewidth=2.5, label="Nilakantha")
plt.plot(N_suave, pi_monte_carlo_suave, linewidth=2.5, label="Monte Carlo")
plt.plot(N_suave, pi_machin_suave, linewidth=2.5, label="Machin")
plt.plot(N_suave, pi_chudnovsky_suave, linewidth=2.5, label="Chudnovsky")

plt.scatter(N_leibniz, pi_leibniz_resultados, s=45, edgecolor="black", zorder=3)
plt.scatter(N_nilakantha, pi_nilakantha_resultados, s=45, edgecolor="black", zorder=3)
plt.scatter(N_monte_carlo, pi_monte_carlo_resultados, s=45, edgecolor="black", zorder=3)
plt.scatter(N_machin, pi_machin_resultados, s=45, edgecolor="black", zorder=3)
plt.scatter(N_chudnovsky, pi_chudnovsky_resultados, s=45, edgecolor="black", zorder=3)

plt.axhline(PI_REF, linestyle="--", linewidth=2, label="Valor de pi")

configurar_grafico_padrao()
salvar_figura("figura_08_curvas_suavizadas_com_pontos.png")
