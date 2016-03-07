# Преамбула

import os
import matplotlib.pyplot as plt

def save(name='', fmt='png'):
    pwd = os.getcwd()
    os.chdir('./pictures')
    plt.savefig('%s.png' % name, fmt='png')
    os.chdir(pwd)
    #plt.close()


