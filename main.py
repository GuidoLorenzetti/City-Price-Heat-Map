import numpy as np
import csv
import matplotlib.pyplot as plt

def pos(r,l,lat,dist):
  x = -1
  i = r
  while i < l:
    x += 1
    if float(lat) > i and float(lat) < (i + dist):
      break
    i += dist
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
  dist_hor = int(abs((r - l) / inter))
  dist_ver = int(abs((u - d) / inter))
  return (r,l,u,d,dist_hor,dist_ver)

long=0.001

with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    r,l,d,u,dist_hor,dist_ver = lat_long(reader,long)
    cant = np.zeros((dist_hor,dist_ver))
    price = np.zeros((dist_hor,dist_ver))
    price_prom = np.zeros((dist_hor,dist_ver))
  
with open('listings.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
      if row[0] == "id":
        continue
      x = pos (r,l,row[6],long)
      y = pos (u,d,row[7],long)
      cant[((x-1),(y-1))] += 1
      price[((x-1),(y-1))] += float(row[9])

for l in range(dist_hor):
  for m in range (dist_ver):
    if cant[(l, m)] != 0:
      price_prom[(l, m)] = price[(l, m)] / cant[(l, m)]

figure, axes = plt.subplots()
map = axes.pcolormesh(price_prom, cmap='hot', vmin=0, vmax=2000)
axes.set_title('Heat Map')
plt.axis('off')
cbar = figure.colorbar(map)
cbar.ax.tick_params(size=0)
plt.show()