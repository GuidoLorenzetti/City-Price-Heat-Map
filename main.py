import numpy as np
import csv
import matplotlib.pyplot as plt

def pos(r,l,lat,dist_hor):
  x = -1
  i = r
  while i < l:
    x += 1
    if float(lat) > i and float(lat) < (i + dist_hor):
      break
    i += dist_hor
  return x

def lat_long(reader,inter):
  cont = 0
  for row in reader:
    if row[0] == "id":
          continue
    else:
      if cont == 0:
        r = float(row[6])
        l = float(row[6])
        u = float(row[7])
        d = float(row[7])
      else:
        if float(row[6]) < r:
          r = float(row[6])
        if float(row[6]) > l:
          l = float(row[6])
        if float(row[7]) < d:
          d = float(row[7])
        if float(row[7]) > u:
          u = float(row[7])
      cont += 1
  dist_hor = abs((r - l) / inter)
  dist_ver = abs((u - d) / inter)
  return (r,l,u,d,dist_hor,dist_ver)

inter = 200

cant = np.zeros((inter, inter))
precio = np.zeros((inter, inter))
precio_prom = np.zeros((inter, inter))
cont = 0

with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    r,l,d,u,dist_hor,dist_ver = lat_long(reader,inter)

with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
      if row[0] == "id":
        continue
      x = pos (r,l,row[6],dist_hor)
      y = pos (u,d,row[7],dist_ver)
      cant[((x-1),(y-1))] += 1
      precio[((x-1),(y-1))] += float(row[9])
      cont += 1

for l in range(inter):
  for m in range (inter):
    if cant[(l, m)] != 0:
      precio_prom[(l, m)] = precio[(l, m)] / cant[(l, m)]

figure, axes = plt.subplots()
precio_prom = axes.pcolormesh(precio_prom, cmap='hot', vmin=0, vmax=2000)
axes.set_title('Heat Map')
figure.colorbar(precio_prom)
plt.show()