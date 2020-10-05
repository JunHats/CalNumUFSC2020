from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5, 6]


Dkscnt = [28.12158166796831, 23.071457086035398, 20.908235751433086,
          20.553434187943733,  20.531886612497512, 20.531689232720325]


Dk_minusOnescnt = [45, 28.12158166796831, 23.071457086035398,
                   20.908235751433086, 20.553434187943733,  20.531886612497512]


Dknm = [29.19624064472574, 21.81053777956228,  20.56803099349769,
        20.531687584699874,  20.531689129629104, 0]


Dk_minusOnenm = [50, 29.19624064472574, 21.81053777956228,
                 20.56803099349769, 20.531687584699874, 0]


plt.plot(x, Dkscnt, label="Dk(Secante)")
plt.plot(x, Dk_minusOnescnt, label="Dk-1(Secante)")
plt.plot(x, Dknm, label="Dk(Newton)")
plt.plot(x, Dk_minusOnenm, label="Dk-1nm(Newton)")


plt.legend(loc='upper left')

plt.tight_layout()


plt.show()
