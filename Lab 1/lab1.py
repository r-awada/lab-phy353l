import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
import numpy as np


def gaus(x, a, b, c):
    return a*np.exp((-(x-b)**2)/(2 * c**2))


def gaus2(x, a, b, c, d, e, f):
    return a*np.exp(-(x-b)*(x-b)/(2 * c*c)) + d*np.exp(-(x-e)*(x-e)/(2 * f*f))


def FUN():
    # Import all data
    tube1 = pd.read_csv("tube1trunc.csv")
    tube2 = pd.read_csv("tube2trunc.csv")
    tube3 = pd.read_csv("tube3trunc.csv")
    tube4 = pd.read_csv("tube4trunc.csv")
    table1 = dict()
    table2 = dict()
    table3 = dict()
    table4 = dict()
    # Save all data trials into tables of tube
    for i in range(1, 4):
        table1[f"x{i}"] = tube1[f'HD spec {i} wave'].tolist()
        table1[f"y{i}"] = tube1[f'HD spec {i} intensity'].tolist()
        table2[f"x{i}"] = tube2[f'H spec {i} wave'].tolist()
        table2[f"y{i}"] = tube2[f'H spec {i} intensity'].tolist()
        table3[f"x{i}"] = tube3[f'HD spec {i} wave'].tolist()
        table3[f"y{i}"] = tube3[f'HD spec {i} intensity'].tolist()
        table4[f"x{i}"] = tube4[f'H spec {i} wave'].tolist()
        table4[f"y{i}"] = tube4[f'H spec {i} intensity'].tolist()
    x = table1['x1']
    
    # Compute average of each tube
    table1['Average Intensity'] = tube1['HD average intensity'].tolist()
    table2['Average Intensity'] = tube2['H average intensity'].tolist()
    table3['Average Intensity'] = tube3['HD average intensity'].tolist()
    table4['Average Intensity'] = tube4['H average intensity'].tolist()

    colors = ['green', 'blue', 'red', 'orange']
    labels = ['trial 1', 'trial 2', 'trial 3']


    pguess4 = [5900, 655.82, 5E-2]
    pguess2 = [5900, 655.82, 5E-2]
    pguess1 = [5900, 655.82, 5E-2, 3000,655.6,5E-2]
    pguess3 = [5900, 655.82, 5E-2, 2000,655.6,5E-2]

    params4, pcov4 = spy.curve_fit(
        gaus,x, table4['Average Intensity'], p0=pguess4)
    params2, pcov2 = spy.curve_fit(
        gaus,x, table2['Average Intensity'], p0=pguess2)
    params1, pcov1 = spy.curve_fit(
        gaus2,x, table1['Average Intensity'], p0=pguess1)
    params3, pcov3 = spy.curve_fit(
        gaus2,x, table3['Average Intensity'], p0=pguess3)
    
    params31, pcov31 = spy.curve_fit(
        gaus2,x, table3['y1'], p0=pguess3)
    params32, pcov32 = spy.curve_fit(
        gaus2,x, table3['y2'], p0=pguess3)
    params33, pcov33 = spy.curve_fit(
        gaus2,x, table3['y3'], p0=pguess3)
    params11, pcov11 = spy.curve_fit(
        gaus2,x, table1['y1'], p0=pguess3)
    params12, pcov12 = spy.curve_fit(
        gaus2,x, table1['y2'], p0=pguess3)
    params13, pcov13 = spy.curve_fit(
        gaus2,x, table1['y3'], p0=pguess3)

    peak3 = dict()
    peak3[1] = abs(params31[1]-params31[4])
    peak3[2] = abs(params32[1]-params32[4])
    peak3[3] = abs(params33[1]-params33[4])
    uncer31 = pcov31[1][1]**(1/2)
    uncer32 = pcov32[1][1]**(1/2)
    uncer33 = pcov33[1][1]**(1/2)
    uncer311 = pcov31[4][4]**(1/2)
    uncer312 = pcov32[4][4]**(1/2)
    uncer313 = pcov33[4][4]**(1/2)

    uncertainty3 = dict()
    uncertainty3[1] = (uncer31**2 + uncer311**2)**(1/2)
    uncertainty3[2] = (uncer32**2 + uncer312**2)**(1/2)
    uncertainty3[3] = (uncer33**2 + uncer313**2)**(1/2)
    total_uncertainty = 0
    total_wave_diff = 0
    final_uncertainty = 0
    for i in range(1,4):
        print(f"For Tube 3 Trial {i} the difference in wavelength is")
        print(f"{peak3[i]} +/- {uncertainty3[i]} nm")
        print()
        total_uncertainty += uncertainty3[i]
        total_wave_diff += uncertainty3[i]*peak3[i]
        final_uncertainty += (1/(uncertainty3[i]))**2

    uncer11 = pcov11[1][1]**(1/2)
    uncer12 = pcov12[1][1]**(1/2)
    uncer13 = pcov13[1][1]**(1/2)
    uncer211 = pcov11[4][4]**(1/2)
    uncer212 = pcov12[4][4]**(1/2)
    uncer213 = pcov13[4][4]**(1/2)
    uncertainty1 = dict()
    uncertainty1[1] = (uncer11**2 + uncer211**2)**(1/2)
    uncertainty1[2] = (uncer12**2 + uncer212**2)**(1/2)
    uncertainty1[3] = (uncer13**2 + uncer213**2)**(1/2)
    peak1 = dict()
    peak1[1] = abs(params11[1]-params11[4])
    peak1[2] = abs(params12[1]-params12[4])
    peak1[3] = abs(params13[1]-params13[4])
    for i in range(1,4):
        print(f"For Tube 1 Trial {i} the difference in wavelength is")
        print(f"{peak1[i]} +/- {uncertainty1[i]} nm")
        print()
        total_uncertainty += uncertainty1[i]
        total_wave_diff += uncertainty1[i]*peak1[i]
        final_uncertainty += (1/(uncertainty1[i]))**2
    final_uncertainty = 1/final_uncertainty**(1/2)
    print(f"The total wave difference is {total_wave_diff/total_uncertainty} +/- {final_uncertainty}")

    func1 = {1:[],2:[],3:[]}
    func3 = {1:[],2:[],3:[]}



    x_strawberry = np.linspace(x[0],x[-1],10000)

    # Compute y values for guess and model
    for i in x_strawberry:
        func1[1].append(gaus2(i, *params11))
        func1[2].append(gaus2(i, *params12))
        func1[3].append(gaus2(i, *params13))
        func3[1].append(gaus2(i, *params31))
        func3[2].append(gaus2(i, *params32))
        func3[3].append(gaus2(i, *params33))


    #Plot model and guess and data 
    for i in range(1,4):
        plt.plot(x_strawberry, func1[i], 'b--', label="Fitted Model")
        if i ==1:
            plt.plot(x, table1['y1'],'go', label=f'Trial {i}')
        elif i ==2:
            plt.plot(x, table1['y2'],'go', label=f'Trial {i}')
        else:
            plt.plot(x, table1['y3'],'go', label=f'Trial {i}')
        plt.legend(loc="upper left")
        plt.title(f'Tube1 Trial{i} Intensity vs Wavelength')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity')
        plt.show()

    for i in range(1,4):
        plt.plot(x_strawberry, func3[i], 'b--', label="Fitted Model")
        if i ==1:
            plt.plot(x, table3['y1'],'go', label=f'Trial {i}')
        elif i ==2:
            plt.plot(x, table3['y2'],'go', label=f'Trial {i}')
        else:
            plt.plot(x, table3['y3'],'go', label=f'Trial {i}')
        plt.legend(loc="upper left")
        plt.title(f'Tube3 Trial{i} Intensity vs Wavelength')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity')
        plt.show()
    return


FUN()
