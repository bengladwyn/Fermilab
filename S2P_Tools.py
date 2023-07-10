# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
def plot(filename):
    frequency, s11_mag, s11_phase, s21_mag, s21_phase = parameters(filename)
    plot_parameters(filename,frequency, s11_mag, s11_phase, s21_mag, s21_phase)

# %%
def parameters(filename, plot_data=False):
    # Read the data from the text file
    data = np.loadtxt(filename, skiprows=5)

    with open(filename, 'r') as file:
        header = file.readlines()[4]

    # Check if "RI" or "MA" is present in the 5th line
    if "RI" in header:
        frequency = data[:, 0]
        s11_mag = np.abs(data[:, 1]+1j*data[:, 2])
        s11_phase = np.angle(data[:, 1]+1j*data[:, 2], deg=True)
        s21_mag = np.abs(data[:, 3]+1j*data[:, 4])
        s21_phase = np.angle(data[:, 3]+1j*data[:, 4], deg=True)
        s12_mag = np.abs(data[:, 5]+1j*data[:, 6])
        s12_phase = np.angle(data[:, 5]+1j*data[:, 6], deg=True)
        s22_mag = np.abs(data[:, 7]+1j*data[:, 8])
        s22_phase = np.angle(data[:, 7]+1j*data[:, 8], deg=True)
    elif "MA" in header:
        frequency = data[:, 0]
        s11_mag = data[:, 1]
        s11_phase = data[:, 2]
        s21_mag = data[:, 3]
        s21_phase = data[:, 4]
        s12_mag = data[:, 5]
        s12_phase = data[:, 6]
        s22_mag = data[:, 7]
        s22_phase = data[:, 8]
    
    if plot_data == True:
        plot(filename)
    
    return frequency, s11_mag, s11_phase, s21_mag, s21_phase

'''
# Plot S12 magnitude and phase
axs[2, 0].plot(frequency, s12_mag)
axs[2, 0].set_title('S12 Magnitude')
axs[2, 0].set_xlabel('Frequency (Hz)')
axs[2, 0].set_ylabel('Magnitude (dB)')

axs[2, 1].plot(frequency, s12_phase, color='orange', linewidth=0.8)
axs[2, 1].set_title('S12 Phase')
axs[2, 1].set_xlabel('Frequency (Hz)')
axs[2, 1].set_ylabel('Phase (degrees)')

# Plot S22 magnitude and phase
axs[3, 0].plot(frequency, s22_mag)
axs[3, 0].set_title('S22 Magnitude')
axs[3, 0].set_xlabel('Frequency (Hz)')
axs[3, 0].set_ylabel('Magnitude (dB)')

axs[3, 1].plot(frequency, s22_phase, color='orange', linewidth=0.8)
axs[3, 1].set_title('S22 Phase')
axs[3, 1].set_xlabel('Frequency (Hz)')
axs[3, 1].set_ylabel('Phase (degrees)')
'''


# %%
def plot_parameters(title,frequency, s11_mag, s11_phase, s21_mag, s21_phase):    
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    print(title)
    # Plot S11 magnitude and phase
    axs[0, 0].plot(frequency, s11_mag)
    axs[0, 0].set_title('$s_{11}$ Magnitude', size=10)
    axs[0, 0].set_xlabel('Frequency (Hz)', size=8)
    axs[0, 0].set_ylabel('Magnitude', size=8)

    axs[0, 1].plot(frequency, s11_phase, color='orange', linewidth=0.8)
    axs[0, 1].set_title('$s_{11}$ Phase', size=10)
    axs[0, 1].set_xlabel('Frequency (Hz)', size=8)
    axs[0, 1].set_ylabel('Phase (degrees)', size=8)

    # Plot S21 magnitude and phase
    axs[1, 0].plot(frequency, s21_mag)
    axs[1, 0].set_title('$s_{21}$ Magnitude', size=10)
    axs[1, 0].set_xlabel('Frequency (Hz)', size=8)
    axs[1, 0].set_ylabel('Magnitude', size=8)

    axs[1, 1].plot(frequency, s21_phase, color='orange', linewidth=0.8)
    axs[1, 1].set_title('$s_{21}$ Phase', size=10)
    axs[1, 1].set_xlabel('Frequency (Hz)', size=8)
    axs[1, 1].set_ylabel('Phase (degrees)', size=8)
    
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    plt.show()


