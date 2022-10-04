import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np


def LABLAB():

    def recur2(x):
        if x == 1:
            return 1
        else:
            return x * recur2(x-1)

    def recur(x):
        if len(x) == 1:
            return 1
        else:
            return x[-1] * recur(x[:-1])

    def poison(x, mu):
        return poisson.pmf(x, mu)

    def poisson2(x, mu):
        return (np.exp(-1* mu)*mu**x)/recur2(x)
    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')
    tall2 = pd.read_csv('tall100.csv')
    tall3 = pd.read_csv('tall1000.csv')
    short1= pd.read_csv('short50.csv')
    short2= pd.read_csv('short500.csv')

    tall50counts = {'title':'Tall Occurance of Counts with 50 ms Integration Time over 10 s', "guess":[3]}
    tall100counts = {'title':'Tall Occurance of Counts with 500 ms Integration Time over 100 s', "guess":[5]}
    tall1000counts = {'title':'Tall Occurance of Counts with 1s Integration Time over 200 s', "guess":[20]}
    short50counts = {'title':'Short Occurance of Counts with 50 ms Integration Time over 10 s',"guess":[17]}
    short500counts= {'title':'Short Occurance of Counts with 500 ms Integration Time over 100 s',"guess":[150]}

    data = [tall50counts, tall100counts, tall1000counts, short50counts, short500counts]

    def ploth(histo, title, binz, guess):
        hist = plt.hist(histo,bins = binz)
        x = [int(i) for i in hist[1]][1::]
        y = [int(i) for i in hist[0]]
        #print(params, pcov)
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count Number measured')
        plt.title(title)
        #x = np.linspace(0,x[-1],100)
        params, pcov = spy.curve_fit(poison, x, y,p0=guess)
        return params, pcov, x

    def plotp(x, params, title, label0):
        x = np.linspace(0,x[-1],1000)
        plt.plot(x,poison(x,*params), label = label0)
        plt.legend(loc="upper left")
        plt.title(title)
        

    for i in range(1,4):
        tall50counts[i] = tall1[f"count{i}"].tolist()
        tall100counts[i] = tall2[f"count{i}"].tolist()
        tall1000counts[i] = tall3[f"count{i}"].tolist()
        short50counts[i] = short1[f"count{i}"].tolist()
        short500counts[i] = short2[f"count{i}"].tolist()

    for i in data:
        for j in range(1,4):
            i[f"params{j}"], i[f"pcov{j}"], i[f"x{j}"] = ploth(i[j], i['title'], max(i[j]), i['guess'])
        plt.show()
    for i in data:
        for j in range(1,4):
            plotp(i[f"x{j}"], i[f"params{j}"], i['title'], f"Trial {j}")
            #plotp(i[f"x{j}"],*i['guess'], i['title'], 'guess')
            print(i[f"pcov{j}"])
        plt.show()




LABLAB()
