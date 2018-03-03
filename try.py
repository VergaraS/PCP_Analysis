# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 12:08:51 2018

@author: Santiago
"""

arch = 'C:\\Users\\Santiago\\Downloads\\SANTIVERGARABECH'
arch2 = 'C:\\Users\\Santiago\\Downloads\\SANTIVERGARABECH2.txt'
arch3 = 'C:\\Users\\Santiago\\Downloads\\CelsiaSolar.csv'

import numpy as np
import pandas as pd
from datetime import datetime,timedelta 

f = open(arch,'r+')


lista = []
for i in range(5):
    c=f.readline()
    lista.append(c)
    print(c)

año = int(lista[4][59:64])

xxx = datetime(2018,3,3)

g = np.loadtxt(arch2)


h = pd.read_table(arch2)


j = pd.read_csv(arch3)
j = j.set_index('Fecha')
j.to_csv('C:\\Users\\Santiago\\Downloads\\CelsiaSolar2.csv')