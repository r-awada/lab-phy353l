from droplet import *
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy
import scipy.stats as stats
import math


def gaus2(x, a, b, c, d, e, f):
    return a*np.exp(-(x-b)*(x-b)/(2 * c*c)) + d*np.exp(-(x-e)*(x-e)/(2 * f*f))


def chi_dsit(chi, dof):
    return (chi**((dof/2)-1) * np.exp(-chi/2))/(2**(dof/2) * scipy.special.gamma((dof)/2))


def chi_squared(y_expec, y_val, sigma):
    ans = 0
    for num, i in enumerate(y_val):
        if i != 0:
            ans += (1/sigma[num])**2 * (i-y_expec[num])**(2)
    return ans


def main():

    data = pd.read_csv('data.csv')
    data = data["time"].tolist()
    drops = []

    def make_drops(data, drops):
        num = 1
        curr = drop(40, [], [], 26)
        for i in data:
            if math.isnan(i):
                drops.append(curr)
                if len(drops) < 22:
                    curr = drop(40, [], [], 25)
                else:
                    curr = drop(60, [], [], 26)
                num = 1
            elif num == 2:
                curr.rise.append(i)
                num = 1
            else:
                curr.fall.append(i)
                num += 1
        for i in drops:
            i.fall_vel()
            i.rise_vel()
            i.drag()
            i.radi()
            i.charge()
            i.charge_per_mass()
    make_drops(data, drops)
    binz = np.linspace(0, max(i.q for i in drops), 19)
    entries, bin_edges, patches = plt.hist([i.q for i in drops], bins=binz)
    uncer = [(i**(1/2)) for i in entries]
    bin_middles = (bin_edges[1:] + bin_edges[:-1])/2
    plt.xlabel('Average Charge Measured Per Droplet (Coulombs)')
    plt.ylabel('Count of Droplets')
    plt.title('Histogram of Average Charge Per Droplet')
    plt.show()
    print(f"The total number of drops we recorded was {len(drops)}")

    guess = [8, 1.6e-19, 0.7e-19, 4, 3.2e-19, 0.2e-19]
    params, pcov = spy.curve_fit(gaus2, bin_middles, entries, p0=guess)
    print(params)
    pcov = (np.diag(pcov))
    x = np.linspace(0, 5e-19, 1000)
    plt.plot(x, gaus2(x, *params))
    plt.hist([i.q for i in drops], bins=binz)
    plt.xlabel('Average Charge Measured Per Droplet (Coulombs)')
    plt.ylabel('Count of Droplets')
    plt.title('Function Fit Over Histogram')
    plt.show()

    dof = sum(entries) - 1
    print(dof)
    binz = np.linspace(0, max(i.q for i in drops), 40)
    entries, bin_edges, patches = plt.hist([i.q for i in drops], bins=binz)
    uncer = [(i**(1/2)) for i in entries]
    bin_middles = (bin_edges[1:] + bin_edges[:-1])/2
    plt.clf()
    x = np.linspace(10, dof+20, 200)
    y = [chi_dsit(i, dof) for i in x]
    y_expec = [gaus2(i, *params) for i in bin_middles]
    chi = chi_squared(y_expec, entries, uncer)
    plt.plot(x, y)
    print(chi)
    plt.axvline(x=chi, color="blue", label='Chi-Squared Value', linestyle='--')
    big = scipy.stats.chi2.ppf(1-.05, df=dof)
    small = scipy.stats.chi2.ppf(.05, df=dof)
    plt.axvline(x=big, color="black")
    plt.axvline(x=small, color="black")
    plt.legend(loc="upper right")
    plt.title('Chi-Squared Distribution and Chi-Squared Value of Fit')
    plt.xlabel("Chi-Squared")
    plt.ylabel("Probabilty Distribution of Chi Squared")
    plt.show()
    pcov = [i**(1/2) for i in pcov]
    print(pcov)



main()
