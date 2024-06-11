#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

directorio = Path('D:\\Datos NOMAD\\OCS_upper_limits')

def leer_ficheros_salida(directorio):
    datos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.txt'):
            ruta = os.path.join(directorio, archivo)
            with open(ruta, 'r') as filename:
                for linea in filename.readlines()[1:]:
                    columns = linea.split()
                    altura = float(columns[0])
                    vmr = float(columns[1])
                    datos.append((altura, vmr))
    
    datos_df = pd.DataFrame(datos, columns=['altura', 'vmr'])
    return datos_df

def plot_graf(datos):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    
    ax.tick_params(axis='both', which='both', labelsize=12)
    
    hb=ax.hexbin(datos['vmr'], datos['altura'], gridsize=50, cmap='Wistia', mincnt=1, xscale='log')
    
    ax.set_ylim(0, 80)
    ax.set_xlim(0.1, 1000)
    ax.set_xlabel(u'OCS upper limit [ppbv]', fontsize=12)
    ax.set_ylabel(u'Altitude [km]',fontsize=12)
    folder = f"Ampliacion_orden_134/Figuras"
    fig.savefig(f'{folder}/'
                           f'OCS_Figure.png', bbox_inches='tight')
    #plt.colorbar(hb, ax=ax)
    #plt.show()
    return fig, ax


#··············································································································
# Lee los datos de todos los archivos del directorio
'''datos = leer_ficheros_salida(directorio)
# Dibuja el gráfico
plot_graf(datos)'''

