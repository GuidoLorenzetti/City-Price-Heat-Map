import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

def pos(r,l,lat,dist_hor):
  x = -1
  i = r
  while i < l:
    if lat > i and lat < (i - dist_hor):
      return x
    i = i - dist_hor
    x += 1

lat_izq = 55.733342
lat_der = 55.614935
long_arr = 12.423467
long_ab = 12.686726
inter = 50

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
        x = pos (lat_der,lat_izq,float(row[6]),dist_hor)
        y = pos (long_arr,long_ab,float(row[7]),dist_ver)
        cant[(x, y)] += 1
        precio[(x, y)] += float(row[9])

for l in range(inter):
  for m in range (inter):
    if cant[(l, m)] != 0:
      precio_prom[(l, m)] = precio[(l, m)] / cant[(l, m)]

for l in range(inter):
      print(precio_prom[(l, 24)])


figure, axes = plt.subplots()
precio_prom = axes.pcolormesh(precio_prom, cmap='inferno', vmin=0, vmax=2000)
axes.set_title('Copenhagen Heat Map')
figure.colorbar(precio_prom)
#inferno
plt.show()
