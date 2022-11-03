from element import *
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy
import scipy.stats as stats
import math


def relativity2(k):
    m = 9.1093837e-31
    c = 299792458
    return (k**2)/(2*m*c**2) + k


def main():

    names = ["Na22", "Cs137", "Co60", "Co57", "Mn54", "Ba133"]
    peaks = [511, 661.657, 1332.492, 122.06065, 834.848, 356.0129]
    peaks2 = [1274.537, 0, 1173.228, 0, 0, 80.9979]
    data = pd.read_csv('data.csv')
    elements = []
    for num, i in enumerate(names):
        y = data[i].tolist()
        splice = 0
        while y.index(max(y[splice:])) < 29:
            splice += 1
        elements.append(element(i, y[splice:], peaks[num]))
        elements[num].axis()

    elements[0].compton(45, 65, 87, 97)
    elements[0].compton2(236, 258, 273, 289)
    elements[1].compton(84, 107, 128, 136)
    elements[2].compton(185, 208, 225, 235)
    elements[2].compton2(289, 292, 293, 301)
    elements[4].compton(109, 144, 167, 183)
    elements[5].compton(14, 19, 23, 31)

    for i in elements:
        plt.plot(i.x, i.y)
        plt.title(f"Gamma Ray Energy Distribution for {i.name}")
        plt.xlabel('Energy (keV)')
        plt.ylabel('Counts')
        try:
            plt.axvline(x=i.comp, color="black")
            plt.axvline(x=i.comp2, color="black")
        except:
            pass
        plt.show()

    x = np.linspace(0, 2e-13, 100000)
    y = [relativity2(i) for i in x]
    plt.plot(x, y, label="Relativity")
    plt.xlabel('Energy')
    plt.ylabel('P^2/2m')
    plt.title('Energy Momentum Relationship')
    for num, i in enumerate(elements):
        try:
            # print(f"{i.name} has p^2 of {relativity2(i.comp)}")
            plt.plot(i.comp*1.6022e-16, i.rela(peaks[num]),
                     marker="o", markersize=10, label=i.name)
        except Exception as e:
            print(e)
            pass

    plt.legend(loc="upper left")
    plt.plot(x, x, label="Newton")
    plt.show()


main()
