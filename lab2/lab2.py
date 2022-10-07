import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
from scipy.stats import poisson
import numpy as np
import scipy

def LABLAB():

    def poison(x, mu):
        return poisson.pmf(x, mu)

    #import data for the fun of it
    tall1 = pd.read_csv('tall50.csv')
    tall2 = pd.read_csv('tall500.csv')
    tall3 = pd.read_csv('tall1000.csv')
    short1= pd.read_csv('short50.csv')
    short2= pd.read_csv('short500.csv')
    short3= pd.read_csv('short1000.csv')

    tall50counts = {'title':'Tall Occurance of Counts with 50 ms Integration Time of 10 s', "guess":[1]}
    tall500counts = {'title':'Tall Occurance of Counts with 500 ms Integration Time of 100 s', "guess":[3]}
    tall1000counts = {'title':'Tall Occurance of Counts with 1s Integration Time of 200 s', "guess":[23]}
    short50counts = {'title':'Short Occurance of Counts with 50 ms Integration Time of 10 s',"guess":[2]}
    short500counts= {'title':'Short Occurance of Counts with 500 ms Integration Time of 100 s',"guess":[23]}
    short1000counts= {'title':'Short Occurance of Counts with 1s Integration Time of 100 s',"guess":[23]}

    data = [tall50counts, tall500counts, tall1000counts]
    paired_data= {0:short50counts,1:short500counts,2:short1000counts}

    def chi_dsit(chi,nu):
        return (chi**(-1/2) * np.exp(-chi/2))/(2**(1/2) * scipy.special.gamma(1/2))

    def chi_squared(y_pois, y_val, sigma, N):
        ans = 0
        for i in y_val:
            ans += 1/sigma * (i-poison(i,y_pois))**(2)
        return ans
    def ploth(histo, title, binz, guess, label0):
        h = np.histogram(histo,bins=binz)
        entries, bin_edges, patches= plt.hist(histo,bins = binz,density=True,label=label0)
        uncer = [i**(1/2)/sum(h[0]) for i in h[0]]
        print(uncer)
        plt.ylabel('Occurance of Counts')
        plt.xlabel('Count Number measured')
        plt.title(title)
        plt.legend(loc="upper left")
        bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])
        params, pcov = spy.curve_fit(poison,bin_middles, entries,p0=guess,sigma=uncer)
        print(pcov)
        return params, pcov, entries, uncer 

    def plotp(params, title, label0, entries, uncer):
        x_fun = np.arange(len(entries))
        x = np.linspace(0,len(entries),100)
        plt.plot(x,poison(x,*params),'-', label = label0)
        #print(np.trapz(poison(x_fun,*params)))
        plt.plot(np.arange(len(entries)),entries,"o",label= "Original"+label0 )
        #plt.errorbar(np.arange(len(entries)),entries, yerr= uncer )
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
        for j in range(1,2):
            i[f'bins{j}'] = np.arange(max(i[j])) -0.5
            i[f"params{j}"], i[f"pcov{j}"], i[f"entries{j}"], i[f"uncer{j}"] = ploth(i[j], i['title'], i[f'bins{j}'], i['guess'], f"Trial{j}")
            paired_data[num][f'bins{j}'] = np.arange(max(paired_data[num][j])) -0.5
            paired_data[num][f"params{j}"], paired_data[num][f"pcov{j}"], paired_data[num][f"entries{j}"], paired_data[num][f"uncer{j}"]= ploth(paired_data[num][j], paired_data[num]['title'], paired_data[num][f'bins{j}'], paired_data[num]['guess'], f"Trial{j}")
        plt.show()
    for num, i in enumerate(data):
        for j in range(1,2):
            plotp(i[f"params{j}"], i['title'], f"Trial {j}", i[f"entries{j}"], i[f"uncer{j}"])
            plotp(paired_data[num][f"params{j}"], paired_data[num]['title'], f"Trial {j}", paired_data[num][f"entries{j}"], paired_data[num][f"uncer{j}"])
            #plotp(i[f"x{j}"],*i['guess'], i['title'], 'guess')
        plt.show()




LABLAB()
