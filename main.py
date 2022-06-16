import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

def lat(r,l,lat,dist_hor):
  x = 0
  i = r
  while i < l:
    if lat > i and lat < (i - dist_hor):
      return x
    i = i - dist_hor
    x += 1

def long(u,d,long,dist_ver):
  y = 0
  j = u
  while j < d:
    if long > j and long < (j - dist_ver):
      return y
    j = j - dist_ver
    y += 1

lat_izq = 55.733342
lat_der = 55.614935
long_arr = 12.423467
long_ab = 12.686726
inter = 7

dist_hor = (lat_der - lat_izq) / inter
dist_ver = (long_arr - long_ab) / inter

cant = np.zeros((inter, inter))
precio = np.zeros((inter, inter))
precio_prom = np.zeros((inter, inter))
print (cant)
print (precio)
print(precio_prom)

with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        if row[0] == "id":
          continue
        x = lat (lat_der,lat_izq,float(row[6]),dist_hor)
        y = long (long_arr,long_ab,float(row[7]),dist_ver)
        cant[(x-1, y-1)] += 1
        precio[(x-1, y-1)] += float(row[9])

for l in range(inter):
  for m in range (inter):
    if cant[(l, m)] != 0:
      precio_prom[(l, m)] = precio[(l, m)] / cant[(l, m)]

print (cant)
print (precio)
print(precio_prom)

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
