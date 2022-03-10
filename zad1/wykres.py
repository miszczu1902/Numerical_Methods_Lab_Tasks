import matplotlib.pyplot as plt


def rysuj_wykres(x0, fx0, x, y):
    plt.plot(x, y)
    plt.scatter(x0, fx0, c='r')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(-11, 20)
    plt.text(x0, fx0, str(x0))
    plt.show()

# def rysuj_wykres1(a, b, c, tabX, tabY):
#     x = np.linspace(0, 7, 100)
#     if c == 0:
#         y = a * x + b
#     else:
#         y = a * x ** 2 + b * np.sin(x) + c
#     plt.plot(x, y, '-b', label='y = ax')
#     plt.scatter(tabX, tabY, c='r')
#     plt.xlabel("X")
#     plt.ylabel("f(X)")
#     plt.show()
#
#
# def rysuj_wykres2(tabX, tabX2, tabY, tabFX):
#     ax = plt.axes(projection='3d')
#     ax.plot_trisurf(tabX.flatten(), tabX2.flatten(), tabFX.flatten())
#     ax.scatter(tabX, tabX2, tabY, color="r")
#     ax.set_xlabel('X1')
#     ax.set_ylabel('X2')
#     ax.set_zlabel('FX')
#     plt.show()
#
#
# def rysuj_histogram(tabX, tabY):
#     plt.hist(tabX - tabY, 50)
#     plt.xlabel("Wartosc")
#     plt.ylabel("Ilosc wystapien")
#     plt.grid(True)
#     plt.show()
