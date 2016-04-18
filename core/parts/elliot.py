import numpy as np
import matplotlib.pyplot as plt
import os
import pywt

elliot_waves = []
wavelets = pywt.families()


def showPlot(date, data, file_name):
    fig, ax = plt.subplots()
    ax.plot(date, data)
    fig.savefig(file_name)
    plt.close(fig)


# def generate_elliot_waves(folder):

common_folder = 'static/results/'
folder_name = 'elliot/'


def trend(data):
    return 0 * np.arange(len(data))


def print_wave(data, file_name):
    date = np.arange(len(data))
    return showPlot(date, data, file_name)


def print_fft(data, file_name):
    A = np.fft.fft(data)
    frrAbs = np.abs(A)
    return print_wave(frrAbs, file_name)


def get_filter(arr):
    return list([x for x in arr])


def print_wavelet(data, wavelet_name, filter, file_name):
    result = pywt.dwt(data, wavelet_name)
    if filter == 'high':
        return print_wave(result[0], file_name)
    elif filter == 'low':
        return print_wave(result[1], file_name)


def build_elliot_waves(path):
    x = [1, 3, 2, 4]
    z = [1, 3, 2, 4, 3, 5]
    # print('lol1', os.path.abspath(path))
    if not os.path.exists(os.path.abspath(path)):
        os.makedirs(os.path.abspath(path))
    minus_x = np.subtract(np.max(x), x)
    minus_z = np.subtract(np.max(z), z)

    # print_wave(x, trend, path + 'x.png')
    elliot_waves.append('x')
    # print_wave(z, trend, path + 'z.png')
    elliot_waves.append('z')

    # print_wave(minus_x, trend, path + 'minus_x.png')
    elliot_waves.append('minus_x')
    # print_wave(minus_z, trend, path + 'minus_z.png')
    elliot_waves.append('minus_z')

    # print_fft(z, trend, 'fft.png')
    # print_wavelet(z, trend, 'coif1', 'high', 'db.png')


# build_elliot_waves('static/results/elliot/')

def generate_elliot_waves(scale=4):
    import random
    w1 = np.zeros(6)
    w2 = np.zeros(4)

    w1[1] = int(random.randint(3, scale))
    print(w1[1])
    w1[2] = int(random.randint(1, w1[1]-1))
    valid = True
    while valid:
        temp = int(random.randint(1, 3)) * int(random.randint(1, scale))
        print(w1[1], w1[2], temp)
        if w1[1] >= w1[2] + temp:
            continue
        w1[3] = int(random.randint(w1[1], w1[2] + temp))
        if(w1[3] - w1[2]) > w1[1]:
            valid = False
    w1[4] = int(random.randint(w1[1], w1[3]))
    w1[5] = w1[4] + w1[1]

    print(w1)
    w2[0] = w1[5]
    valid = True
    while valid:
        try:
            w2[3] = int(random.randint(w1[4] + 1, w1[5] - 2))
            w2[2] = int(random.randint(w2[3] + 1, w1[5] - 1))
            w2[1] = int(random.randint(w2[3] + 1, w2[2] - 1))
            valid = False
        except Exception:
            _ = 1
    print(w1, w2)
    result = list(w1) + list(w2)[1:]
    print(result)
    return result

z = [ 0.,  3.,  2.,  6.,  5.,  8.]
mx = [10, 11, 9]
print_wave(generate_elliot_waves(50), 'zx.png')
# print_wave(z, 'zx.png')


# def generate_elliot_wave