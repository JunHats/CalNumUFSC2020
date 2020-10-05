from math import e


def f(d):
    return ((0.01328) * (d**2) * (4.47**3) - 500)


def secante(D0, D1, Erro, max_iter):
    k = 1
    Da1 = D0
    D = D1
    print("k\t\t D\t\t\t f(D)")
    while(k <= max_iter):
        Da2 = Da1
        Da1 = D
        D = Da1 - f(Da1)*(Da2 - Da1)/(f(Da2) - f(Da1))
        print(f'{k}\t{D}\t{f(D)}')
        if(abs(D - Da1) <= Erro):
            return (D, k)
        k += 1


D0 = 50
D1 = 45
Erro = e**-5
max_iter = 50

solucao = secante(D0, D1, Erro, max_iter)

print(f'O valor da raíz é: {solucao[0]}')
print(f'O número de iterações realizadas foi: {solucao[1]}')
