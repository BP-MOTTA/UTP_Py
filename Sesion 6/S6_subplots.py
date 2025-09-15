import matplotlib.pyplot  as plt
import numpy as np


ejex=[i for i in range(30)] #crear numeros del 0 al 29
ejey=np.cos(ejex)
ejey2=-ejey

fig,axs = plt.subplots(2)
fig.suptitle("datos por separado")
axs[0].plot(ejex,ejey,'g-o',label="datos de tiempo de sueño")
axs[1].plot(ejex,ejey2,'r-x',label="datos de tiempo de juego")
plt.show()

