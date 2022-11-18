from qibo import gates
from qibo.models import Circuit
import numpy as np
import matplotlib.pyplot as plt


def plot_amplitudes(amplitudes, p=False):
    amplitudes = amplitudes.state()
    states = []
    amp = []
    for i in range(int(len(amplitudes)/2)):
        states.append("{0:0{bits}b}".format(i, bits=int(np.log2(len(amplitudes)/2))))
    for i in range(0, len(amplitudes), 2):
        amp.append((1/np.sqrt(2))*(np.real(amplitudes[i])-np.real(amplitudes[i+1])))
    if p:
        print(amp)
    fig = plt.figure(figsize = (18,6))
    width = 0.5
    plt.title('Amplitudes', fontdict={'fontsize': 14})
    plt.xlabel('state', fontsize=14)
    plt.ylabel('magnitude', fontsize=14)
    plt.ylim(-1.1,1.1)
    plt.bar(states, amp, color='C0', width=width)
    plt.grid()
    plt.show()