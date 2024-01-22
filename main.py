#import library Numerical Python
import numpy as np
#Import library pandas
import pandas as pd
#Import pandas
import math
#Import library untuk membuat grafik
import matplotlib.pyplot as plt
#Import drive untuk mengakses Google Drive
from google.colab import drive
drive.mount('/content/drive')
#Simpan data excel menjadi object ke dalam variabel data_telur 
data_telur=pd.read_excel('/content/data_telur_surabaya.xlsx')
#Tampilkan head dari data tersebut
data_telur.head()
#Tampilkan data x
x=data_telur['Data']
x
#Tampilkan dan decrale data y
y=data_telur['Harga']
y
# Mencari Interpolosai Linear pada index ke 82

print(f" {y[80]} + (( {y[82]} - {y[80]}) / ({x[82]} - {x[80]})) * ({x[81]} - {x[80]})")

resultOfInterpolationLinear = y[80] + (( y[82] - y[80]) / (x[82] - x[80])) * (x[81] - x[80])

resultOfInterpolationLinear

#Mengcek terlebih dahulu apakah benar data y pada index 82 itu kosong atau tidak ? jika iya maka assign dan carilah RKT Linear

print(f"is it 0 ? = {y[81]}")

y[81] = resultOfInterpolationLinear

y[81]

#Print semua data untuk memastikan lagi
singbox = 1
for harganya in data_telur['Harga']:
  print(f"{singbox} . {harganya}")
  singbox += 1

# Menghitung Rkt Linear

x=data_telur['Data']
y=data_telur['Harga']
rata_x=np.mean(x)
rata_y=np.mean(y)
print("Nilai rata-rata dari x=",rata_x)
print("Nilai rata-rata dari y=",rata_y)

n=len(x)
xy=0
sigma_x=0
sigma_y=0
x2=0

for i in range(n) :
  xy += x[i]*y[i]
  sigma_x += x[i]
  sigma_y += y[i]
  x2 += x[i]**2

print("Nilai xy = ",xy)
print("Nilai sigma x =",sigma_x)
print("Nilai sigma y =",sigma_y)
print("Sigma x kuadrat =",x2)

atas=(n*xy)-(sigma_x*sigma_y)
bawah=(n*x2)-((sigma_x)**2)
b=atas/bawah
print("Nilai b =",b)
a=rata_y-(b*rata_x)
print("Nilai a =",a)
RKT_y=a+b*x
print("Nilai fungsi =",RKT_y)

#Scatter plot untuk data asli
plt.scatter(x,y)

#Grafik RKT
plt.plot(x,RKT_y)
plt.title('Regresi Kuadrat Terkecil (Linier)')
plt.xlabel('Data')
plt.ylabel('Harga')
plt.legend(['Real','RKT Linier'])
plt.show()

# Menghitung Koefisien Korelasi
Dt2=0
D2=0

for j in range(n) :
  Dt2 += (y[j]-rata_y)**2
  D2 += (y[j]-a-b*x[j])**2

r2=(Dt2-D2)/Dt2
print("Nilai koefisien korelasi=",r2)