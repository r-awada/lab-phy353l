import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
import numpy as np


def LABLAB():
    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')
    tall2 = pd.read_csv('tall100.csv')
    tall3 = pd.read_csv('tall1000.csv')

    tall50counts = dict()
    tall100counts = dict()
    tall1000counts = dict()

    for i in range(1,4):
        tall50counts[i] = tall1[f"count{i}"].tolist()
        tall100counts[i] = tall2[f"count{i}"].tolist()
        tall1000counts[i] = tall3[f"count{i}"].tolist()
        hist = plt.hist(tall50counts[i], bins=max(tall1[f"count{i}"]))
        hist = plt.hist(tall100counts[i], bins=max(tall2[f"count{i}"]))
        hist = plt.hist(tall1000counts[i], bins=max(tall3[f"count{i}"]))
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count within wait 50 ms')
        plt.show()


LABLAB()
