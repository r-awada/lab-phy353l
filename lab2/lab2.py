import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
import numpy as np


def LABLAB():
    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')

    tall50counts = dict()

    for i in range(1,4):
        tall50counts[i] = tall1[f"count{i}"].tolist()
        hist = plt.hist(tall50counts[i], bins=max(tall1[f"count{i}"]))
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count within wait 50 ms')
        plt.show()


LABLAB()
