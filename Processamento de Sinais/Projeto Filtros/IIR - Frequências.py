import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import butter
from scipy.signal import cheby1
from scipy.signal import cheby2

# FFT do sinal de entrada e saída
def plot_fft(number, sinal, Fs, title):
    N = len(sinal)
    f = np.fft.fftfreq(N, 1/Fs)
    F_sinal = np.fft.fft(sinal)
    plt.subplot(4, 1, number)
    plt.plot(f[:N//2], np.abs(F_sinal)[:N//2])
    plt.title(title)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.legend()

# Lendo o arquivo de som
som, Fs = sf.read('/home/joaopalopes/Development/Masters-Degree/Processamento de Sinais/Projeto Filtros/audio.wav') # Sampling frequency and audio data

# Parâmetros do filtro
wc = 0.1  # Frequência de corte normalizada

# Passa-baixas

# Projeto dos filtros IIR (Butterworth, Chebyshev 1 e Chebyshev 2)
b_butter, a_butter = butter(11, wc, btype='low', analog=False, output='ba', fs=Fs)
b_cheby1, a_cheby1 = cheby1(4, 0.5, wc, btype='low', analog=False, output='ba', fs=Fs)
b_cheby2, a_cheby2 = cheby2(4, 0.5, wc, btype='low', analog=False, output='ba', fs=Fs)

# Resposta em frequência
w, H_butter = signal.freqz(b_butter, a_butter, worN=8000)
w, H_cheby1 = signal.freqz(b_cheby1, a_cheby1, worN=8000)
w, H_cheby2 = signal.freqz(b_cheby2, a_cheby2, worN=8000)

# Plotando as respostas em frequência (módulo e fase)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(H_butter)), 'b', label='Butterworth')
plt.plot(w, 20 * np.log10(abs(H_cheby1)), 'r', label='Chebyshev I')
plt.plot(w, 20 * np.log10(abs(H_cheby2)), 'g', label='Chebyshev II')
plt.title('Resposta em Frequência (Magnitude)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(H_butter)), 'b', label='Butterworth')
plt.plot(w, np.unwrap(np.angle(H_cheby1)), 'r', label='Chebyshev I')
plt.plot(w, np.unwrap(np.angle(H_cheby2)), 'g', label='Chebyshev II')
plt.title('Resposta em Frequência (Fase)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.legend()

plt.tight_layout()
plt.show()

# Gerando sinal multisenoidal com 8 tons
tons = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500]  # Frequências dos tons
t = np.linspace(0, 1, Fs)  # 1 segundo de duração
sinal_entrada = np.sum([np.sin(2 * np.pi * f * t) for f in tons], axis=0)

# Filtrando o sinal
sinal_filtrado_butter = np.convolve(sinal_entrada, H_butter, mode='same')
sinal_filtrado_cheby1 = np.convolve(sinal_entrada, H_cheby1, mode='same')
sinal_filtrado_cheby2 = np.convolve(sinal_entrada, H_cheby2, mode='same')

# Plotando os espectros de frequência
plt.figure()
plot_fft(1, sinal_entrada, Fs, 'Espectro de Frequência - Entrada')

plot_fft(2, sinal_filtrado_butter, Fs, 'Espectro de Frequência - Saída (Butterworth)')
plot_fft(3, sinal_filtrado_cheby1, Fs, 'Espectro de Frequência - Saída (Chebyshev I)')
plot_fft(4, sinal_filtrado_cheby2, Fs, 'Espectro de Frequência - Saída (Chebyshev II)')

plt.tight_layout()
plt.show()

# Passa-altas

# Projeto dos filtros IIR (Butterworth, Chebyshev 1 e Chebyshev 2)
b_butter, a_butter = butter(11, wc, btype='high', analog=False, output='ba', fs=Fs)
b_cheby1, a_cheby1 = cheby1(4, 0.5, wc, btype='high', analog=False, output='ba', fs=Fs)
b_cheby2, a_cheby2 = cheby2(4, 0.5, wc, btype='high', analog=False, output='ba', fs=Fs)

# Resposta em frequência
w, H_butter = signal.freqz(b_butter, a_butter, worN=8000)
w, H_cheby1 = signal.freqz(b_cheby1, a_cheby1, worN=8000)
w, H_cheby2 = signal.freqz(b_cheby2, a_cheby2, worN=8000)


# Plotando as respostas em frequência (módulo e fase)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(H_butter)), 'b', label='Butterworth')
plt.plot(w, 20 * np.log10(abs(H_cheby1)), 'r', label='Chebyshev I')
plt.plot(w, 20 * np.log10(abs(H_cheby2)), 'g', label='Chebyshev II')
plt.title('Resposta em Frequência (Magnitude)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(H_butter)), 'b', label='Butterworth')
plt.plot(w, np.unwrap(np.angle(H_cheby1)), 'r', label='Chebyshev I')
plt.plot(w, np.unwrap(np.angle(H_cheby2)), 'g', label='Chebyshev II')
plt.title('Resposta em Frequência (Fase)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.legend()

plt.tight_layout()
plt.show()

# Gerando sinal multisenoidal com 8 tons
tons = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500]  # Frequências dos tons
t = np.linspace(0, 1, Fs)  # 1 segundo de duração
sinal_entrada = np.sum([np.sin(2 * np.pi * f * t) for f in tons], axis=0)

# Filtrando o sinal
sinal_filtrado_butter = np.convolve(sinal_entrada, H_butter, mode='same')
sinal_filtrado_cheby1 = np.convolve(sinal_entrada, H_cheby1, mode='same')
sinal_filtrado_cheby2 = np.convolve(sinal_entrada, H_cheby2, mode='same')

# Plotando os espectros de frequência
plt.figure()
plot_fft(1, sinal_entrada, Fs, 'Espectro de Frequência - Entrada')

plot_fft(2, sinal_filtrado_butter, Fs, 'Espectro de Frequência - Saída (Butterworth)')
plot_fft(3, sinal_filtrado_cheby1, Fs, 'Espectro de Frequência - Saída (Chebyshev I)')
plot_fft(4, sinal_filtrado_cheby2, Fs, 'Espectro de Frequência - Saída (Chebyshev II)')

plt.tight_layout()
plt.show()
