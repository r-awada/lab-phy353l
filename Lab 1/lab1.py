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
        table1[f"hd_wave_{i}"] = tube1[f'HD spec {i} wave'].tolist()
        table1[f"hd_intensity_{i}"] = tube1[f'HD spec {i} intensity'].tolist()
        table2[f"h_wave_{i}"] = tube2[f'H spec {i} wave'].tolist()
        table2[f"h_intensity_{i}"] = tube2[f'H spec {i} intensity'].tolist()
        table3[f"hd_wave_{i}"] = tube3[f'HD spec {i} wave'].tolist()
        table3[f"hd_intensity_{i}"] = tube3[f'HD spec {i} intensity'].tolist()
        table4[f"h_wave_{i}"] = tube4[f'H spec {i} wave'].tolist()
        table4[f"h_intensity_{i}"] = tube4[f'H spec {i} intensity'].tolist()
    x = table1['hd_wave_1']
    
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
    
    guess2 = []
    func2 = []
    func4 = []
    guess4 = []
    func1 = []
    guess1 = []
    func3 = []
    guess3 = []
    x_strawberry = np.linspace(x[0],x[-1],10000)

    # Compute y values for guess and model
    for i in x_strawberry:
        guess2.append(gaus(i, *pguess2))
        func2.append(gaus(i, *params2))
        guess4.append(gaus(i, *pguess4))
        func4.append(gaus(i, *params4))
        guess1.append(gaus2(i, *pguess1))
        func1.append(gaus2(i, *params1))
        guess3.append(gaus2(i, *pguess3))
        func3.append(gaus2(i, *params3))


    #Plot model and guess and data 
    plt.plot(x_strawberry, func4, 'b--', label="Function Fun time")
    plt.plot(x_strawberry, guess4, 'r--', label='Guess')
    plt.plot(x, table4['Average Intensity'],
             'yo', label='Tube 4')
    plt.legend(loc="upper left")
    plt.title('Average Intensity of Tube4')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    print('Guess for tube 4 \n', params4, pcov4)
    plt.show()
    
    plt.plot(x_strawberry, func2, 'b--', label="Function Fun time")
    plt.plot(x_strawberry, guess2, 'r--', label='Guess')
    plt.plot(x, table2['Average Intensity'],
             'yo', label='Tube 2')
    plt.legend(loc="upper left")
    plt.title('Average Intensity of Tube2')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    print('Guess for tube2 \n', params2, pcov2)
    plt.show()

    plt.plot(x_strawberry, func1, 'b--', label="Function Fun time")
    plt.plot(x_strawberry, guess1, 'r--', label='Guess')
    plt.plot(x, table1['Average Intensity'],
             'yo', label='Tube 1')
    plt.legend(loc="upper left")
    plt.title('Average Intensity of Tube1')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    print('Guess for tube1 \n', params1, pcov1)
    plt.show()

    plt.plot(x_strawberry, func3, 'b--', label="Function Fun time")
    plt.plot(x_strawberry, guess3, 'r--', label='Guess')
    plt.plot(x, table3['Average Intensity'],
             'yo', label='Tube 3')
    plt.legend(loc="upper left")
    plt.title('Average Intensity of Tube3')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    print('Guess for tube3 \n', params3, pcov3)
    plt.show()
    print()
    print("The Difference in Wavelengths tube 1")
    print(params1[1]-params1[4])
    print()
    print("The Difference in Wavelengths tube 3")
    print(params3[1]-params3[4])
   # plt.plot(table1['hd_wave_1'], table1['Average Intensity'],
   #          'gx', label='Tube 1')
   # plt.plot(table1['hd_wave_1'], table2['Average Intensity'],
   #          'r^', label='Tube 2')
   # plt.plot(table1['hd_wave_1'], table3['Average Intensity'],
   #          'b*', label='Tube 3')
   # plt.plot(table1['hd_wave_1'], table4['Average Intensity'],
   #          'yo', label='Tube 4')
   # plt.title('Average Intensity of All Tubes')
   # plt.xlabel('Wavelength (nm)')
   # plt.ylabel('Intensity')
   # plt.legend(loc="upper left")
   # plt.show()
   # for i in range(1, 4):
   #     plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"],
   #              color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
   # print('made plt for tube1')
   # plt.title('HD Intensity vs Wavelength for Tube 1')
   # plt.xlabel('Wavelength (nm)')
   # plt.ylabel('Intensity')
   # plt.legend(loc="upper left")
   # plt.show()
   # for i in range(1, 4):
   #     plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"],
   #              color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
   # print('made plt for tube2')
   # plt.title('H Intensity vs Wavelength Tube 2')
   # plt.xlabel('Wavelength (nm)')
   # plt.ylabel('Intensity')
   # plt.legend(loc="upper left")
   # plt.show()

   # for i in range(1, 4):
   #     plt.plot(table3[f"hd_wave_{i}"], table3[f"hd_intensity_{i}"],
   #              color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
   # print('made plt for tube3')
   # plt.title('H Intensity vs Wavelength Tube 3')
   # plt.xlabel('Wavelength (nm)')
   # plt.ylabel('Intensity')
   # plt.legend(loc="upper left")
   # plt.show()

   # for i in range(1, 4):
   #     plt.plot(table4[f"h_wave_{i}"], table4[f"h_intensity_{i}"],
   #              color=colors[i-1], linestyle='dashed', linewidth=1, label=labels[i-1])
   # print('made plt for tube4')
   # plt.title('H Intensity vs Wavelength Tube 4')
   # plt.xlabel('Wavelength (nm)')
   # plt.ylabel('Intensity')
   # plt.legend(loc="upper left")
   # plt.show()
   # for i in range(1, 4):
   #     plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"],
   #              color=colors[i-1], linestyle='dashed', linewidth=1, label='H')
   #     plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"],
   #              color=colors[i], linestyle='dashed', linewidth=1, label='HD')
   #     plt.title(f'Trial {i} Intensity vs Wavelength for H and HD')
   #     plt.xlabel('Wavelength (nm)')
   #     plt.ylabel('Intensity')
   #     plt.legend(loc="upper left")
   #     plt.show()
   # print('Plotted both samples or smt idk dawg')
    return


FUN()
