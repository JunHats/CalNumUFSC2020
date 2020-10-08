from numpy import array, zeros, fabs
a = array([[76.0, -25.0, -50.0, 0.0, 0.0, 0.0],
           [-25, 56, -1, -30, 0, 0],
           [-50, -1, 106, -54, 0, 0],
           [0, -30, -55, 159, -25, -50],
           [0, 0, 0, -25, 56, -1],
           [0, 0, 0, -50, -1, 106]])

b = array([10.0, 0.0, 0.0, 0.0, 0.0, 0.0])

n = len(b)
x = zeros(n, float)




def gaussianElimination(a, x, b, n):
    for k in range(n-1):
        if fabs(a[k, k]) == 0:
            for i in range(k+1, n):
                if fabs(a[i, k]) > fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k+1, n):
            if a[i, k] == 0:
                continue

            factor = a[k, k]/a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - b[i] * factor

    print(a)
    print(b)

   
    x[n-1] = b[n-1] / a[n-1, n-1]

    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i, j] * x[j]
        x[i] = (b[i] - sum_ax)/a[i, i]

    print('The solution of the System: ')
    print(x)


gaussianElimination(a, x, b, n)
