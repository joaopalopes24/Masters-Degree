import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.signal import butter
from scipy.signal import cheby1
from scipy.signal import cheby2
from scipy.signal import lfilter

# Função para calcular a FFT e plotar o espectro
def fftf(x, Fs):
    N = len(x)
    T = N / Fs
    freq = np.fft.fftfreq(N, d=1/Fs)
    X = np.fft.fft(x) / N
    cutOff = N // 2
    freq = freq[:cutOff]
    X = np.abs(X[:cutOff])

    plt.figure()
    plt.plot(freq, X)
    plt.title('Espectro de Frequências do Sinal (FFT)')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Lendo o arquivo de som
som, Fs = sf.read('/home/joaopalopes/Development/Masters-Degree/Processamento de Sinais/Projeto Filtros/audio.wav') # Sampling frequency and audio data
left = som[:, 0]  # Canal esquerdo
right = som[:, 1]  # Canal direito

# Plotando o espectro de frequências
fftf(som[:, 0], Fs)

# Normalizando a frequência de corte
Fc = 2000 # Frequência de corte (Hz)
wc = Fc / (Fs / 2)  # Frequência de corte normalizada

# Projeto dos filtros IIR (Butterworth, Chebyshev 1 e Chebyshev 2)
b_butter, a_butter = butter(11, wc, btype='low', analog=False)
b_cheby1, a_cheby1 = cheby1(4, 0.5, wc, btype='low', analog=False)
b_cheby2, a_cheby2 = cheby2(8, 20, wc, btype='low', analog=False)

# Filtra os sinais
y1_butter = lfilter(b_butter, a_butter, left)
y2_butter = lfilter(b_butter, a_butter, right)
y_butter = np.column_stack((y1_butter, y2_butter))

# Reproduzindo o áudio filtrado
sd.play(y_butter, Fs)

# Plotando o espectro do sinal filtrado
fftf(y_butter[:, 0], Fs)

# Filtra os sinais
y1_cheby1 = lfilter(b_cheby1, a_cheby1, left)
y2_cheby1 = lfilter(b_cheby1, a_cheby1, right)
y_cheby1 = np.column_stack((y1_cheby1, y2_cheby1))

# Reproduzindo o áudio filtrado
sd.play(y_cheby1, Fs)

# Plotando o espectro do sinal filtrado
fftf(y_cheby1[:, 0], Fs)

# Filtra os sinais
y1_cheby2 = lfilter(b_cheby2, a_cheby2, left)
y2_cheby2 = lfilter(b_cheby2, a_cheby2, right)
y_cheby2 = np.column_stack((y1_cheby2, y2_cheby2))

# Reproduzindo o áudio filtrado
sd.play(y_cheby2, Fs)

# Plotando o espectro do sinal filtrado
fftf(y_cheby2[:, 0], Fs)