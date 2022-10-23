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
                if len(drops)< 22:
                    curr = drop(40,[],[],25)
                else:
                    curr = drop(60,[],[],26)
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
            i.charge_per_mass()
    make_drops(data, drops)
    binz = np.linspace(0,5e-19,30)
    plt.hist([i.q for i in drops], bins=binz)
    plt.xlabel('Average Charge Measured Per Droplet (Coulombs)')
    plt.ylabel('Count of Droplets')
    plt.title('Histogram of Average Charge Per Droplet')
    plt.show()
    print(f"The total number of drops we recorded was {len(drops)}")


main()
