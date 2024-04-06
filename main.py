import matplotlib.pyplot as plt
import numpy as np

fileobj = open("1kHz_44100Hz_16bit_05sec.wav", mode = "rb")

data = fileobj.read()
#print(data)

file_size_inbutes = data[4:8]
file_size = int.from_bytes(file_size_inbutes, byteorder="little")
#print(file_size_inbutes)
#print(file_size)

num_of_channels_in_byte = data[22:24]
num_of_channels = int.from_bytes(num_of_channels_in_byte, byteorder="little")
#print(num_of_channels)

audio_data_size = data[40:44]
audio_data = int.from_bytes(audio_data_size, byteorder="little")
#print(audio_data)

sample_rate_in_byte = data[24:28]
sample_rate = int.from_bytes(sample_rate_in_byte, byteorder="little")


audio_amps = []

for i in range(0, audio_data, 2):
    amp_in_byte = data [44+i:i+46]
    amp = int.from_bytes(amp_in_byte, byteorder="little", signed = True)
    audio_amps.append(amp)

#print(audio_amps)

xdata_time = np.linspace(0, len(audio_amps)/sample_rate, len(audio_amps))
#xdata_freqs = 

spectre = np.fft.fft(audio_amps)
abs_spectre = abs(spectre)

plt.plot(xdata, abs_spectre)
plt.show()