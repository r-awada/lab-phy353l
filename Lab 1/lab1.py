import pandas as pd
import matplotlib.pyplot as plt


def FUN():
    tube1 = pd.read_csv("tube1.csv")
    tube2 = pd.read_csv("tube2.csv")
    table1 = dict()
    table2 = dict()
    for i in range(1,4):
        table1[f"hd_wave_{i}"] = tube1[f'HD spec {i} wave'].tolist()
        table1[f"hd_intensity_{i}"] = tube1[f'HD spec {i} intensity'].tolist()
        table2[f"h_wave_{i}"] = tube2[f'H spec {i} wave'].tolist()
        table2[f"h_intensity_{i}"] = tube2[f'H spec {i} intensity'].tolist()

    colors=['green','blue','red', 'orange']
    labels=['trial 1', 'trial 2', 'trial 3']
    for i in range(1,4):
        plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"], color=colors[i-1], linestyle='dashed',linewidth=1, label=labels[i-1])
    print('made plt for tube1')
    plt.title('HD Intensity vs Wavelength for Tube 1')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()
    for i in range(1,4):
        plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"], color=colors[i-1], linestyle='dashed',linewidth=1, label=labels[i-1])
    print('made plt for tube2')
    plt.title('H Intensity vs Wavelength Tube 2')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.legend(loc="upper left")
    plt.show()

    for i in range(1,4):
        plt.plot(table2[f"h_wave_{i}"], table2[f"h_intensity_{i}"], color=colors[i-1], linestyle='dashed',linewidth=1, label='H')
        plt.plot(table1[f"hd_wave_{i}"], table1[f"hd_intensity_{i}"], color=colors[i], linestyle='dashed',linewidth=1, label='HD')
        plt.title(f'Trial {i} Intensity vs Wavelength for H and HD')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity')
        plt.legend(loc="upper left")
        plt.show()
    print('Plotted both samples or smt idk dawg')
    return


FUN()
