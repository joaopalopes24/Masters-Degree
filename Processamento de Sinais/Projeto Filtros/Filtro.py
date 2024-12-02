import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

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

# Função para filtro passa-baixa ideal
def ideal_lp(wc, M):
    alpha = (M - 1) / 2
    n = np.arange(M)
    m = n - alpha + np.finfo(float).eps
    hd = np.sin(wc * m) / (np.pi * m)
    return hd

# Lendo o arquivo de som
som, Fs = sf.read('/home/joaopalopes/Development/Masters-Degree/Processamento de Sinais/Projeto Filtros/audio.wav') # Sampling frequency and audio data
left = som[:, 0]  # Canal esquerdo
right = som[:, 1]  # Canal direito

# Definindo o tempo
tempo = len(left) / Fs
t = np.linspace(0, tempo, len(left))

# Plotando os dados no domínio do tempo
plt.figure()
plt.plot(t, left)
plt.xlabel('Tempo (s)')
plt.ylabel('Potência do Sinal')
plt.title('Sinal')
plt.grid()
plt.show()

# Reproduzindo o áudio
# sd.play(left, Fs)  # Canal esquerdo
# sd.play(right, Fs)  # Canal direito
# sd.play(som, Fs)  # Stereo

# Plotando o espectro de frequências
fftf(som[:, 0], Fs)

# Utilizando a janela de Hanning
M = 448
wc = 0.11 * np.pi  # Frequência de corte em radianos
n = np.arange(M)
w = 0.5 * (1 - np.cos(2 * np.pi * n / (M - 1)))  # Janela de Hanning
hd = ideal_lp(wc, M)
h = hd * w

# Plotando o filtro
plt.figure()
plt.plot(np.linspace(0, Fs / 2, len(h)), np.abs(np.fft.fft(h))[:len(h)])
plt.title('Filtro Especificado')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Filtrando os sinais
y1 = fftconvolve(left, h, mode='same')
y2 = fftconvolve(right, h, mode='same')
y = np.column_stack((y1, y2))

# Reproduzindo o áudio filtrado
sd.play(y, Fs)

# Plotando o espectro do sinal filtrado
fftf(y[:, 0], Fs)
