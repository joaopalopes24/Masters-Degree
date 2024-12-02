import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import firwin
from scipy.signal.windows import get_window

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

# Função para calcular o filtro FIR com uma janela especificada
def fir_filter(wc, M, window_type):
    n = np.arange(M)
    alpha = (M - 1) / 2

    m = n - alpha + np.finfo(float).eps
    hd = np.sin(wc * m) / (np.pi * m)

    window = get_window(window_type, M, fftbins=False)
    hd[int(alpha)] = wc / np.pi  # Corrigir o valor no meio
    
    return hd * window  # Resposta ao impulso do filtro FIR

# Lendo o arquivo de som
som, Fs = sf.read('/home/joaopalopes/Development/Masters-Degree/Processamento de Sinais/Projeto Filtros/audio.wav') # Sampling frequency and audio data

# Parâmetros do filtro
N = 101 # Ordem do filtro
Fc = 2000 # Frequência de corte (Hz)

# Normalizando a frequência de corte
wc = Fc / (Fs / 2)  # Normalizado para firwin (valor entre 0 e 1)

# Calcular o filtro com janelas Hamming, Blackman e Retangular
f_hamming = fir_filter(wc, N, 'hamming')
f_blackman = fir_filter(wc, N, 'blackman')
f_rectangular = fir_filter(wc, N, 'boxcar')

# Resposta em frequência
w, F_hamming = signal.freqz(f_hamming, worN=8000, fs=Fs)
w, F_blackman = signal.freqz(f_blackman, worN=8000, fs=Fs)
w, F_rectangular = signal.freqz(f_rectangular, worN=8000, fs=Fs)

# Plotando as respostas em frequência (módulo e fase)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(F_hamming)), 'b', label='Hamming')
plt.plot(w, 20 * np.log10(abs(F_blackman)), 'r', label='Blackman')
plt.plot(w, 20 * np.log10(abs(F_rectangular)), 'g', label='Rectangular')
plt.title('Resposta em Frequência (Magnitude)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(F_hamming)), 'b', label='Hamming')
plt.plot(w, np.unwrap(np.angle(F_blackman)), 'r', label='Blackman')
plt.plot(w, np.unwrap(np.angle(F_rectangular)), 'g', label='Rectangular')
plt.title('Resposta em Frequência (Fase)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (radianos)')
plt.legend()

plt.tight_layout()
plt.show()

# Calculando o filtro com a função firwin (janelas Hamming, Blackman e Retangular)
h_hamming = firwin(numtaps=N, cutoff=wc, window='hamming', pass_zero='lowpass')
h_blackman = firwin(numtaps=N, cutoff=wc, window='blackman', pass_zero='lowpass')
h_rectangular = firwin(numtaps=N, cutoff=wc, window='rectangular', pass_zero='lowpass')

# Resposta em frequência
w, H_hamming = signal.freqz(h_hamming, worN=8000, fs=Fs)
w, H_blackman = signal.freqz(h_blackman, worN=8000, fs=Fs)
w, H_rectangular = signal.freqz(h_rectangular, worN=8000, fs=Fs)

# Plotando as respostas em frequência (módulo e fase)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(H_hamming)), 'b', label='Hamming')
plt.plot(w, 20 * np.log10(abs(H_blackman)), 'r', label='Blackman')
plt.plot(w, 20 * np.log10(abs(H_rectangular)), 'g', label='Rectangular')
plt.title('Resposta em Frequência (Magnitude)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(H_hamming)), 'b', label='Hamming')
plt.plot(w, np.unwrap(np.angle(H_blackman)), 'r', label='Blackman')
plt.plot(w, np.unwrap(np.angle(H_rectangular)), 'g', label='Rectangular')
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
sinal_filtrado_hamming = np.convolve(sinal_entrada, h_hamming, mode='same')
sinal_filtrado_blackman = np.convolve(sinal_entrada, h_blackman, mode='same')
sinal_filtrado_rectangular = np.convolve(sinal_entrada, h_rectangular, mode='same')

# Plotando os espectros de frequência
plt.figure()
plot_fft(1, sinal_entrada, Fs, 'Espectro de Frequência - Entrada')

plot_fft(2, sinal_filtrado_hamming, Fs, 'Espectro de Frequência - Saída (Hamming)')
plot_fft(3, sinal_filtrado_blackman, Fs, 'Espectro de Frequência - Saída (Blackman)')
plot_fft(4, sinal_filtrado_rectangular, Fs, 'Espectro de Frequência - Saída (Rectangular)')

plt.tight_layout()
plt.show()
