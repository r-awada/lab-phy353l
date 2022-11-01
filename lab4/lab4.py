from element import *
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy
import scipy.stats as stats
import math


def main():

    names = ["Na22", "Cs137", "Co60", "Co57", "Mn54", "Ba133"]
    peaks = [511,661.657,1332.492,122.06065,834.848,356.0129]
    data = pd.read_csv('data.csv')
    elements = []
    for num, i in enumerate(names):
        y = data[i].tolist()
        splice = 0
        while y.index(max(y[splice:])) < 29:
            splice += 1
        elements.append(element(i,y[splice:],peaks[num]))

    for i in elements:
        i.axis()
        i.compton()
        plt.plot(i.x,i.y)
        plt.title(i.name)
        plt.axvline(x=i.comp, color="black")
        plt.show()



main()
