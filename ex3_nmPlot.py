from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]


Dk = [29.19624064472574, 21.81053777956228,  20.56803099349769,
      20.531687584699874,  20.531689129629104]


Dk_minusOne = [50, 29.19624064472574, 21.81053777956228,
               20.56803099349769, 20.531687584699874]

Error = []

for n in range(len(x)):
    Error.append(abs(Dk[n] - Dk_minusOne[n]))
    print(Error)


plt.plot(x, Error, label="Dk - Dk-1")


plt.legend(loc='upper left')

plt.tight_layout()


plt.show()

