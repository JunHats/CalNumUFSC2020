from math import e


def newton_method(f, fl, D0, epsilon, max_inter=50):
    print("k\t\t D\t\t\t f(D)")
    k = 1
    while k <= max_inter:
        D = D0 - f(D0)/fl(D0)
        print(f'{k}\t{D}\t{f(D)}')
        if abs(D-D0) <= epsilon:
            return (D, k)
        D0 = D
        k = k+1
    print("ERRO: num max de iteracoes atingido")
    return D


if __name__ == "__main__":
    def f(d):
        return ((0.01328) * (d**2) * (4.47**3) - 500)

    def fl(d):
        return (2.37*d)


solucao = newton_method(f, fl, 50, e**-5)
print(solucao)

print(f'O valor da raíz é: {solucao[0]}')
print(f'O número de iterações realizadas foi: {solucao[1]}')
