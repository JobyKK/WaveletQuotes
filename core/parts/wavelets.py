from core.parts.indexes import *

common_folder = 'static/results/'
input_plot_name = 'input_plot'
hurst_plot_name = 'hurst_plot'
lyapunov_plot_name = 'lyapunov_plot'
macd_name = 'macd_plot'

def calculateWavelet(wrange, date, x, folder_name, wavelet_name):
    time_scale = int(wrange[:-1])

    plot_name = common_folder + folder_name + '/' + input_plot_name + '.png'
    hurst_name = common_folder + folder_name + '/' + hurst_plot_name + '.png'
    lyapunov_name = common_folder + folder_name + '/' + lyapunov_plot_name + '.png'
    wavelet = next((x for x in all_wavelets if x.__name__ == wavelet_name), None)

    if not os.path.exists(common_folder + folder_name):
        os.makedirs(common_folder + folder_name)
    showPlot(date, x, plot_name)
    showPlot(date, hurst(x), hurst_name)
    print("lyapunov")
    showPlot(date, lyapunov(x), lyapunov_name)
    wa = WaveletAnalysis(data=x, wavelet=wavelet())
    # wavelet power spectrum
    power = wa.wavelet_power
    # scales
    scales = wa.scales
    showResult(date, scales, power, math.ceil(time_scale / 4.), '',
               common_folder + folder_name + '/' + wavelet.__name__ + '.png')
    # except Exception as e:
    #     print('mainLoop', str(e))