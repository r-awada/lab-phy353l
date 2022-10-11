import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy
import scipy.stats as stats

def LABLAB():

    def poison(x, mu):
        return poisson.pmf(x, mu)


    def gaus(x, a, b, c):
        return a*np.exp((-(x-b)**2)/(2 * c**2))


    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')
    tall2 = pd.read_csv('tall500.csv')
    tall3 = pd.read_csv('tall1000.csv')
    short1= pd.read_csv('short50.csv')
    short2= pd.read_csv('short500.csv')
    short3= pd.read_csv('short1000.csv')

    tall50counts = {'title':'ROI1 Occurance of Counts with 50 ms Integration Time of 10 s', "guess":[1], "guess2":[0.38,1,1]}
    tall500counts = {'title':'ROI1 Occurance of Counts with 500 ms Integration Time of 100 s', "guess":[3], "guess2":[0.15,8,2]}
    tall1000counts = {'title':'ROI1 Occurance of Counts with 1s Integration Time of 200 s', "guess":[23], "guess2":[0.19,44,5]}
    short50counts = {'title':'ROI2 Occurance of Counts with 50 ms Integration Time of 10 s',"guess":[2], "guess2":[0.29,2,2]}
    short500counts= {'title':'ROI2 Occurance of Counts with 500 ms Integration Time of 100 s',"guess":[23], "guess2":[0.111,23,3]}
    short1000counts= {'title':'ROI2 Occurance of Counts with 1s Integration Time of 200 s',"guess":[23], "guess2":[0.19,44,5]}

    data = [tall50counts, tall500counts, tall1000counts]
    paired_data= {0:short50counts,1:short500counts,2:short1000counts}
    data2 = [tall50counts, tall500counts, tall1000counts, short50counts,short500counts,short1000counts]



    def ploth(histo, title, binz, guess, label0, guess2):
        h = np.histogram(histo,bins=binz)
        entries, bin_edges, patches= plt.hist(histo,bins = binz,density=True,label=label0)
        uncer = [i**(1/2)/sum(h[0]) for i in h[0]]
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count Number measured')
        plt.title(title)
        plt.legend(loc="upper left")
        bin_middles = 0.5 * (bin_edges[1:]-.5 + bin_edges[:-1]+.5) 
        params, pcov = spy.curve_fit(poison,bin_middles, entries,p0=guess)
        try:
            params2, pcov2 = spy.curve_fit(gaus,bin_middles, entries,p0=guess2)
        except:
            params2, pcov2 = 0, 0
        return params, pcov, entries, uncer, params2, pcov2

    def plotp(params, title, label0, entries, uncer):
        x_fun = np.arange(len(entries))
        x = np.linspace(0,len(entries),100)
        plt.plot(x,poison(x,*params),'-', label = label0)
        plt.plot(np.arange(len(entries)),entries,"o",label= "Original"+label0)
        plt.errorbar(np.arange(len(entries)),entries, yerr= uncer, linestyle='', marker='' )
        plt.legend(loc="upper left")
        plt.title(title)
        

    for i in range(1,4):
        tall50counts[i] = tall1[f"count{i}"].tolist()
        tall500counts[i] = tall2[f"count{i}"].tolist()
        tall1000counts[i] = tall3[f"count{i}"].tolist()
        short50counts[i] = short1[f"count{i}"].tolist()
        short500counts[i] = short2[f"count{i}"].tolist()
        short1000counts[i] = short3[f"count{i}"].tolist()

    for num,i in enumerate(data):
        plt.legend(loc="upper left")
        for j in range(1,4):
            i[f'bins{j}'] = np.arange(max(i[j])) 
            i[f"params{j}"], i[f"pcov{j}"], i[f"entries{j}"], i[f"uncer{j}"], i[f"params2{j}"], i[f"pcov2{j}"] = ploth(i[j], i['title'], i[f'bins{j}'], i['guess'], f"Trial{j}", i[f"guess2"])
            plt.show()
            paired_data[num][f'bins{j}'] = np.arange(max(paired_data[num][j])) 
            paired_data[num][f"params{j}"], paired_data[num][f"pcov{j}"], paired_data[num][f"entries{j}"], paired_data[num][f"uncer{j}"],paired_data[num][f"params2{j}"], paired_data[num][f"pcov2{j}"]= ploth(paired_data[num][j], paired_data[num]['title'], paired_data[num][f'bins{j}'], paired_data[num]['guess'], f"Trial{j}", paired_data[num][f"guess2"])
            plt.show()

    plt.clf()


    for i in data2:
        for j in range(1,4):
            if type(i[f"params{j}"]) != type(0):
                plotp(i[f"params{j}"], i['title'], f"Trial {j}", i[f"entries{j}"], i[f"uncer{j}"])
        plt.show()


    def chi_dsit(chi,dof):
        return (chi**((dof/2)-1) * np.exp(-chi/2))/(2**(dof/2) * scipy.special.gamma((dof)/2))


    def chi_squared(y_pois, y_val, sigma):
        ans = 0
        for num, i in enumerate(y_val):
            if sigma[num] != 0:
                ans += (1/sigma[num])**2 * (i-y_pois[num])**(2)
        return ans


    plt.clf()
    for num, i in enumerate(data2):
        for j in range(1,4):
            dof = len(i[f"entries{j}"]) - 1
            x = np.linspace(0,dof+20,200)
            y = [chi_dsit(p,dof) for p in x]
            y_pois = [poison(p,*i[f"params{j}"]) for p in np.arange(0.5,0.5+len(i[f"entries{j}"]),1)]
            chi = chi_squared(y_pois, i[f"entries{j}"], i[f"uncer{j}"])
            plt.plot(x,y)
            plt.axvline(x = chi, color = "blue", label='Poisson')
            big = scipy.stats.chi2.ppf(1-.05, df=dof)
            small = scipy.stats.chi2.ppf(.05, df=dof)
            plt.axvline(x = big, color = "black")
            plt.axvline(x = small, color = "black")
            if type(i[f"params2{j}"]) != type(0):
                y_pois2 = [gaus(p,*i[f"params2{j}"]) for p in np.arange(0.5,0.5+len(i[f"entries{j}"]),1)]
                chi2 = chi_squared(y_pois2, i[f"entries{j}"], i[f"uncer{j}"])
                plt.axvline(x = chi2, color = "red", label='Gaussian')
            plt.title(f"Trial {j}: "+i['title'])
            plt.legend(loc="upper right")
            plt.xlabel("Chi Squared")
            plt.ylabel("Probabilty Distribution of Chi Squared")
            plt.show()


LABLAB()
