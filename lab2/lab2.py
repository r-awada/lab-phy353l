import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
import numpy as np


def LABLAB():
    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')
    tall2 = pd.read_csv('tall100.csv')
    tall3 = pd.read_csv('tall1000.csv')
    short1= pd.read_csv('short50.csv')
    short2= pd.read_csv('short500.csv')

    tall50counts = {'title':'Tall Occurance of Counts with 50 ms Integration Time over 10 s'}
    tall100counts = {'title':'Tall Occurance of Counts with 500 ms Integration Time over 100 s'}
    tall1000counts = {'title':' Tall Occurance of Counts with 1s Integration Time over 200 s'}


    short50counts = {'title':'Short Occurance of Counts with 50 ms Integration Time over 10 s'}
    short500counts= {'title':'Short Occurance of Counts with 500 ms Integration Time over 100 s'}

    data = [tall50counts, tall100counts, tall1000counts, short50counts, short500counts]

    def plot(histo, title, binz):
        hist = plt.hist(histo,bins = binz)
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count Number measured')
        plt.title(title)


    for i in range(1,4):
        tall50counts[i] = tall1[f"count{i}"].tolist()
        tall100counts[i] = tall2[f"count{i}"].tolist()
        tall1000counts[i] = tall3[f"count{i}"].tolist()
        short50counts[i] = short1[f"count{i}"].tolist()
        short500counts[i] = short2[f"count{i}"].tolist()

    for i in data:
        for j in range(1,4):
            plot(i[j], i['title'], max(i[j]))
        plt.show()


LABLAB()
