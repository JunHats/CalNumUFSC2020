from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5, 6]


Dk = [28.12158166796831, 23.071457086035398, 20.908235751433086,
      20.553434187943733,  20.531886612497512, 20.531689232720325]


Dk_minusOne = [45, 28.12158166796831, 23.071457086035398, 20.908235751433086,
               20.553434187943733,  20.531886612497512]


Error = []

for n in range(len(x)):
    Error.append(abs(Dk[n] - Dk_minusOne[n]))
    print(Error)


plt.plot(x, Error, label="Dk-Dk-1")


plt.legend(loc='upper left')

plt.tight_layout()


plt.show()
