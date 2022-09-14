import pandas as pd
import matplotlib.pyplot as plt


def FUN():
    data = pd.read_csv("Lab1Data.csv")
    print('Imported data')
    hd_wave_1 = data['HD spec 1 wave'].tolist()
    hd_intensity_1 = data['HD spec 1 intensity'].tolist()
    hd_wave_2 = data['HD spec 2 wave'].tolist()
    hd_intensity_2 = data['HD spec 2 intensity'].tolist()
    hd_wave_3 = data['HD spec 3 wave'].tolist()
    hd_intensity_3 = data['HD spec 3 intensity'].tolist()
    print('made all lists')

    plt.plot(hd_wave_1, hd_intensity_1, color='green', linestyle='dashed',linewidth=1)
    plt.plot(hd_wave_2, hd_intensity_2, color='blue', linestyle='dashed',linewidth=1)
    plt.plot(hd_wave_3, hd_intensity_3, color='red', linestyle='dashed',linewidth=1)
    print('made plt')
    plt.show()
    return


FUN()
