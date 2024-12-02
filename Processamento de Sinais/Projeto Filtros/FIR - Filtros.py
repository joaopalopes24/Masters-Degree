import numpy as np
import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.signal import firwin
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

# Lendo o arquivo de som
som, Fs = sf.read('/home/joaopalopes/Development/Masters-Degree/Processamento de Sinais/Projeto Filtros/audio.wav') # Sampling frequency and audio data
left = som[:, 0]  # Canal esquerdo
right = som[:, 1]  # Canal direito

# Plotando o espectro de frequências
fftf(som[:, 0], Fs)

# Parâmetros do filtro
N = 448 # Ordem do filtro
Fc = 2000 # Frequência de corte (Hz)

# Normalizando a frequência de corte
wc = Fc / (Fs / 2)  # Normalizado para firwin (valor entre 0 e 1)

# Calculando o filtro com a função firwin (janelas Hamming, Blackman e Retangular)
h_hamming = firwin(numtaps=N, cutoff=wc, window='hamming', pass_zero='lowpass')
h_blackman = firwin(numtaps=N, cutoff=wc, window='blackman', pass_zero='lowpass')
h_rectangular = firwin(numtaps=N, cutoff=wc, window='rectangular', pass_zero='lowpass')

# Filtrando os sinais
y1 = fftconvolve(left, h_hamming, mode='same')
y2 = fftconvolve(right, h_hamming, mode='same')
y = np.column_stack((y1, y2))

# Reproduzindo o áudio filtrado
sd.play(y, Fs)

# Plotando o espectro do sinal filtrado
fftf(y[:, 0], Fs)

# Filtrando os sinais
y1 = fftconvolve(left, h_blackman, mode='same')
y2 = fftconvolve(right, h_blackman, mode='same')
y = np.column_stack((y1, y2))

# Reproduzindo o áudio filtrado
sd.play(y, Fs)

# Plotando o espectro do sinal filtrado
fftf(y[:, 0], Fs)

# Filtrando os sinais
y1 = fftconvolve(left, h_rectangular, mode='same')
y2 = fftconvolve(right, h_rectangular, mode='same')
y = np.column_stack((y1, y2))

# Reproduzindo o áudio filtrado
sd.play(y, Fs)

# Plotando o espectro do sinal filtrado
fftf(y[:, 0], Fs)