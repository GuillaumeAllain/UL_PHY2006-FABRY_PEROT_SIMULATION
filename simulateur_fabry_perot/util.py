import numpy as np
import matplotlib.pyplot as plt
import hashlib

def plt_trace(space, intensity,title='', **kwargs):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.plot((space-space[0])*1e6, intensity, linewidth=1.5, color='green', **kwargs)
    plt.title(title)
    plt.ylim(0,1)
    plt.xlim(0,((space-space[0])*1e6).max())
    plt.xlabel(r'Variation de distance entre les deux miroirs de la cavité ($\mu m$)')
    plt.ylabel('Intensité relative du champ électrique')
    plt.grid(True)
    ax.set_aspect(1./ax.get_data_ratio())
    plt.show()


