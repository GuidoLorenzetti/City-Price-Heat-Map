import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#with open('listings.csv', newline='') as File:
#reader = csv.reader(File)
#for row in reader:
#print(row[6])

lat_izq = 55.733342
long_arr = 12.423467
lat_der = 55.614935
long_ab = 12.686726
inter = 400

dist_hor = (lat_der - lat_izq) / inter
dist_ver = (long_arr - long_ab) / inter

cant = np.zeros((inter, inter))
precio = np.zeros((inter, inter))
precio_prom = np.zeros((inter, inter))

with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        if row[0] == "id":
            continue
        i = lat_der
        j = long_arr
        x = -1
        y = -1
        while i < lat_izq:
            i = i - dist_hor
            x += 1
            if float(row[6]) > i and float(row[6]) < (i - dist_hor):
                while j < long_ab:
                    y += 1
                    j = j - dist_ver
                    if float(row[7]) > j and float(row[7]) < (j - dist_ver):
                        cant[(x, y)] += 1
                        precio[(x, y)] += float(row[9])

for l in range(inter):
  for m in range (inter):
    if cant[(l, m)] != 0:
      precio_prom[(l, m)] = precio[(l, m)] / cant[(l, m)]


#plt.imshow(precio_prom, cmap='hot', interpolation='nearest', vmin=0, vmax=2000)
#plt.show()

#ax = sns.heatmap(precio_prom, yticklabels=False, vmin=0, vmax=2000)
#plt.show()

figure, axes = plt.subplots()
precio_prom = axes.pcolormesh(precio_prom, cmap='hot', vmin=0, vmax=2000)
axes.set_title('Mapa de Calor de Copenhagen')
figure.colorbar(precio_prom)
#inferno

plt.show()
