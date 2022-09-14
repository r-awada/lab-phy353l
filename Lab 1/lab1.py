import pandas as pd
import matplotlib.pyplot as plt


def FUN():
    tube1 = pd.read_csv("tube1.csv")
    print('Imported tube1')
    hd_wave_1 = tube1['HD spec 1 wave'].tolist()
    hd_intensity_1 = tube1['HD spec 1 intensity'].tolist()
    hd_wave_2 = tube1['HD spec 2 wave'].tolist()
    hd_intensity_2 = tube1['HD spec 2 intensity'].tolist()
    hd_wave_3 = tube1['HD spec 3 wave'].tolist()
    hd_intensity_3 = tube1['HD spec 3 intensity'].tolist()
    print('made all lists for tube1')

    tube1 = pd.read_csv("tube2.csv")
    print('Imported tube2')
    h_wave_1 = tube1['H spec 1 wave'].tolist()
    h_intensity_1 = tube1['H spec 1 intensity'].tolist()
    h_wave_2 = tube1['H spec 2 wave'].tolist()
    h_intensity_2 = tube1['H spec 2 intensity'].tolist()
    h_wave_3 = tube1['H spec 3 wave'].tolist()
    h_intensity_3 = tube1['H spec 3 intensity'].tolist()
    print('made all lists for tube1')

    plt.plot(hd_wave_1, hd_intensity_1, color='green', linestyle='dashed',linewidth=1)
    plt.plot(hd_wave_2, hd_intensity_2, color='blue', linestyle='dashed',linewidth=1)
    plt.plot(hd_wave_3, hd_intensity_3, color='red', linestyle='dashed',linewidth=1)
    print('made plt for tube1')
    plt.show()

    plt.plot(h_wave_1, h_intensity_1, color='green', linestyle='dashed',linewidth=1)
    plt.plot(h_wave_2, h_intensity_2, color='blue', linestyle='dashed',linewidth=1)
    plt.plot(h_wave_3, h_intensity_3, color='red', linestyle='dashed',linewidth=1)
    print('made plt for tube2')
    plt.show()

    plt.plot(hd_wave_1, hd_intensity_1,'r--', label='HD')
    plt.plot( h_wave_1, h_intensity_1, 'b--', label= 'H')
    plt.legend(loc="upper left")
    plt.show()
    print('Plotted both samples or smt idk dawg')

    plt.plot(hd_wave_2, hd_intensity_2,'r--', label='HD')
    plt.plot( h_wave_2, h_intensity_2, 'b--', label= 'H')
    plt.legend(loc="upper left")
    plt.show()
    print('Plotted both samples or smt idk dawg')

    plt.plot(hd_wave_3, hd_intensity_3,'r--', label='HD')
    plt.plot( h_wave_3, h_intensity_3, 'b--', label= 'H')
    plt.legend(loc="upper left")
    plt.show()
    print('Plotted both samples or smt idk dawg')
    return


FUN()
