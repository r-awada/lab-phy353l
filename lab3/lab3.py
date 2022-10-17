from droplet import *
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy
import scipy.stats as stats
import math


def main():

    data = pd.read_csv('data.csv')
    data = data["time"].tolist()
    drops = []

    def make_drops(data, drops):
        num = 1
        curr = drop(40,[],[],26)
        for i in data:
            if math.isnan(i):
                drops.append(curr)
                curr = drop(40,[],[],26)
                num = 1
            elif num ==2:
                curr.rise.append(i)
                num = 1
            else:
                curr.fall.append(i)
                num +=1
        for i in drops:
            i.fall_vel()
            i.rise_vel()
            i.drag()
            i.radi()
            i.charge()
    make_drops(data, drops)

    plt.hist([i.q for i in drops])
    plt.show()


main()
