import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spy
import numpy as np


def gaus(x, a, b, c):
    return a*np.exp(-(x-b)*(x-b)/(2 * c*c))


def FUN():
    tube1 = pd.read_csv("tube1.csv")
    tube2 = pd.read_csv("tube2.csv")
    tube3 = pd.read_csv("tube3.csv")
    tube4 = pd.read_csv("tube4.csv")
    table1 = dict()
    table2 = dict()
    table3 = dict()
    table4 = dict()
    for i in range(1, 4):
        table1[f"hd_wave_{i}"] = tube1[f'HD spec {i} wave'].tolist()
        table1[f"hd_intensity_{i}"] = tube1[f'HD spec {i} intensity'].tolist()
        table2[f"h_wave_{i}"] = tube2[f'H spec {i} wave'].tolist()
        table2[f"h_intensity_{i}"] = tube2[f'H spec {i} intensity'].tolist()
        table3[f"hd_wave_{i}"] = tube3[f'HD spec {i} wave'].tolist()
        table3[f"hd_intensity_{i}"] = tube3[f'HD spec {i} intensity'].tolist()
        table4[f"h_wave_{i}"] = tube4[f'H spec {i} wave'].tolist()
        table4[f"h_intensity_{i}"] = tube4[f'H spec {i} intensity'].tolist()
    table1['Average Intensity'] = tube1['HD average intensity'].tolist()
    table2['Average Intensity'] = tube2['H average intensity'].tolist()
    table3['Average Intensity'] = tube3['HD average intensity'].tolist()
    table4['Average Intensity'] = tube4['H average intensity'].tolist()
    colors = ['green', 'blue', 'red', 'orange']
    labels = ['trial 1', 'trial 2', 'trial 3']

    plt.plot(table1['hd_wave_1'], table1['Average Intensity'],
             'gx', label='Tube 1')
    plt.plot(table1['hd_wave_1'], table2['Average Intensity'],
             'r^', label='Tube 2')
    plt.plot(table1['hd_wave_1'], table3['Average Intensity'],
             'b*', label='Tube 3')
    plt.plot(table1['hd_wave_1'], table4['Average Intensity'],
             'yo', label='Tube 4')
    plt.title('Average Intensity of All Tubes')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()
    params, pcov = spy.curve_fit(
        gaus, table4['Average Intensity'], table1['hd_wave_1'])
    print(params, pcov)
    func = []
    for i in table4['Average Intensity']:
        func.append(gaus(i,params[0],params[1],params[2]))
    plt.plot(table4['h_wave_1'], func)
    plt.plot(table1['hd_wave_1'], table4['Average Intensity'],
             'yo', label='Tube 4')
    plt.show()
    for i in range(1, 4):
        plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"],
                 color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
    print('made plt for tube1')
    plt.title('HD Intensity vs Wavelength for Tube 1')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()
    for i in range(1, 4):
        plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"],
                 color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
    print('made plt for tube2')
    plt.title('H Intensity vs Wavelength Tube 2')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()

    for i in range(1, 4):
        plt.plot(table3[f"hd_wave_{i}"], table3[f"hd_intensity_{i}"],
                 color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
    print('made plt for tube3')
    plt.title('H Intensity vs Wavelength Tube 3')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()

    for i in range(1, 4):
        plt.plot(table4[f"h_wave_{i}"], table4[f"h_intensity_{i}"],
                 color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
    print('made plt for tube4')
    plt.title('H Intensity vs Wavelength Tube 4')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()
    for i in range(1, 4):
        plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"],
                 color=colors[i-1], linestyle='dashed', linewidth=1, label='H')
        plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"],
                 color=colors[i], linestyle='dashed', linewidth=1, label='HD')
        plt.title(f'Trial {i} Intensity vs Wavelength for H and HD')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity')
        plt.legend(loc="upper left")
        plt.show()
    print('Plotted both samples or smt idk dawg')
    return


FUN()
