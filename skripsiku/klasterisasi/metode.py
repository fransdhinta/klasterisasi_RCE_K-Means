import math
from pprint import pprint

# RCE + K-Means

# DATA SEKOLAH

sekolah = [
  {'namaSekolah' : 'SD NEGERI 1 BULULAWANG','X1' : 9,'X2' : 8,'X3' : 1,'X4' : 1,'X5' : 24.14,'X6' : 1.29,},
  {'namaSekolah' : 'SD NEGERI 1 KREBET','X1' : 12,'X2' : 12,'X3' : 2,'X4' : 1,'X5' : 30.50,'X6' : 1.50,},
  {'namaSekolah' : 'SD NEGERI 1 KREBET SENGGRONG','X1' : 5,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 15.83,'X6' : 0.83,},
  {'namaSekolah' : 'SD NEGERI 1 SUDIMORO','X1' : 8,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 19.33,'X6' : 1.33,},
  {'namaSekolah' : 'SD NEGERI 1 WANDANPURO','X1' : 10,'X2' : 10,'X3' : 0,'X4' : 0,'X5' : 24.33,'X6' : 1.67,},
  {'namaSekolah' : 'SD NEGERI 2 BAKALAN','X1' : 8,'X2' : 6,'X3' : 1,'X4' : 0,'X5' : 23.33,'X6' : 1.33,},
  {'namaSekolah' : 'SD NEGERI 2 BULULAWANG','X1' : 6,'X2' : 6,'X3' : 1,'X4' : 1,'X5' : 13.00,'X6' : 1.00,},
  {'namaSekolah' : 'SD NEGERI 2 KASEMBON','X1' : 5,'X2' : 6,'X3' : 0,'X4' : 1,'X5' : 15.33,'X6' : 0.83,},
  {'namaSekolah' : 'SD NEGERI 2 KASRI','X1' : 7,'X2' : 7,'X3' : 0,'X4' : 1,'X5' : 18.00,'X6' : 1.17,},
  {'namaSekolah' : 'SD NEGERI 2 KREBET SENGGRONG','X1' : 10,'X2' : 6,'X3' : 0,'X4' : 1,'X5' : 35.00,'X6' : 1.67,},
  {'namaSekolah' : 'SD NEGERI 2 LUMBANGSARI','X1' : 7,'X2' : 8,'X3' : 0,'X4' : 0,'X5' : 27.17,'X6' : 1.17,},
  {'namaSekolah' : 'SD NEGERI 2 SUDIMORO','X1' : 6,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 17.33,'X6' : 1.00,},
  {'namaSekolah' : 'SD NEGERI 2 WANDANPURO','X1' : 21,'X2' : 15,'X3' : 0,'X4' : 1,'X5' : 29.40,'X6' : 1.40,},
  {'namaSekolah' : 'SD NEGERI 3 KREBET','X1' : 8,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 8.00,'X6' : 1.33,},
  {'namaSekolah' : 'SD NEGERI 3 LUMBANGSARI','X1' : 8,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 24.17,'X6' : 1.33,},
  {'namaSekolah' : 'SD NEGERI 3 SUDIMORO','X1' : 14,'X2' : 14,'X3' : 0,'X4' : 0,'X5' : 21.42,'X6' : 1.17,},
  {'namaSekolah' : 'SD NEGERI 4 WANDANPURO','X1' : 7,'X2' : 6,'X3' : 1,'X4' : 1,'X5' : 34.33,'X6' : 1.17,},
  {'namaSekolah' : 'SD NEGERI GADING','X1' : 8,'X2' : 6,'X3' : 0,'X4' : 0,'X5' : 17.83,'X6' : 1.33,},
  {'namaSekolah' : 'SD NEGERI KUWOLU','X1' : 3,'X2' : 6,'X3' : 0,'X4' : 1,'X5' : 8.50,'X6' : 0.50,},
  {'namaSekolah' : 'SD NEGERI PRINGO','X1' : 6,'X2' : 6,'X3' : 2,'X4' : 2,'X5' : 21.50,'X6' : 1.00,},
]

# NAMA = 'SD NEGERI KU'
# X1 = 4
# X2 = 4
# X3 = 4
# X4 = 4
# X5 = 4
# X6 = 4

# hello = {'namaSekolah' : 'SD NEGERI KU','X1' : X1,'X2' : X2,'X3' : X3,'X4' : X4,'X5' : X5,'X6' : X6,}

# sekolah.append(hello)
# print(sekolah[0]['namaSekolah'])

# PILIH PUSAT CLUSTER AWAL 
cluster1 = sekolah[6]
cluster2 = sekolah[12]

# print(cluster1['namaSekolah'])

# UPDATE PUSAT TITIK KLASTER (RCE)
jarakCluster1 = []
jarakCluster2 = []

for jarak1 in sekolah:
  nama1 = jarak1['namaSekolah']
  jaraknya1 = (((jarak1['X1'] - cluster1['X1'])**2) + ((jarak1['X2'] - cluster1['X2'])**2) + ((jarak1['X3'] - cluster1['X3'])**2) +((jarak1['X4'] - cluster1['X4'])**2) + ((jarak1['X5'] - cluster1['X5'])**2) + ((jarak1['X6'] - cluster1['X6'])**2))
  jarakCluster1.append({'namaSekolah' : nama1, 'X1' : jarak1['X1'], 'X2' : jarak1['X2'],'X3' : jarak1['X3'],'X4' : jarak1['X4'],'X5' : jarak1['X5'],'X6' : jarak1['X6'], 'jarak' : jaraknya1, 'kelompok' : 0})

for jarak2 in sekolah:
  nama2 = jarak2['namaSekolah']
  jaraknya2 = (((jarak2['X1'] - cluster2['X1'])**2) + ((jarak2['X2'] - cluster2['X2'])**2) + ((jarak2['X3'] - cluster2['X3'])**2) +((jarak2['X4'] - cluster2['X4'])**2) + ((jarak2['X5'] - cluster2['X5'])**2) + ((jarak2['X6'] - cluster2['X6'])**2))
  jarakCluster2.append({'namaSekolah' : nama2, 'X1' : jarak2['X1'], 'X2' : jarak2['X2'],'X3' : jarak2['X3'],'X4' : jarak2['X4'],'X5' : jarak2['X5'],'X6' : jarak2['X6'], 'jarak' : jaraknya2, 'kelompok' : 0})

# print(jarakCluster1)

def myFunc(e):
  return e['jarak']

jarakCluster1.sort(key=myFunc)
jarakCluster2.sort(key=myFunc)

# print(jarakCluster1[1]['namaSekolah'])
# print(jarakCluster2[1]['namaSekolah'])

for terdekat in sekolah:
  if terdekat['namaSekolah'] == jarakCluster1[1]['namaSekolah']:
    cluster1 = terdekat

  if terdekat['namaSekolah'] == jarakCluster2[1]['namaSekolah']:
    cluster2 = terdekat

# print(cluster1)
# print(cluster2)

c_cluster1Awal = 0
c_cluster2Awal = 0
c_cluster1Akhir = 1
c_cluster2Akhir = 1

def cmp(a, b):
    return (a > b) - (a < b)

while True:
  if c_cluster1Awal == c_cluster1Akhir and c_cluster2Awal == c_cluster2Akhir: 
    break
  
  jarakCluster1.clear()
  jarakCluster2.clear()
  
  c1 = 0
  c2 = 0

  for jarak1 in sekolah:
    nama1 = jarak1['namaSekolah']
    jaraknya1 = math.sqrt((((jarak1['X1'] - cluster1['X1'])**2) + ((jarak1['X2'] - cluster1['X2'])**2) + ((jarak1['X3'] - cluster1['X3'])**2) +((jarak1['X4'] - cluster1['X4'])**2) + ((jarak1['X5'] - cluster1['X5'])**2) + ((jarak1['X6'] - cluster1['X6'])**2)))
    jarakCluster1.append({'namaSekolah' : nama1, 'X1' : jarak1['X1'], 'X2' : jarak1['X2'],'X3' : jarak1['X3'],'X4' : jarak1['X4'],'X5' : jarak1['X5'],'X6' : jarak1['X6'], 'jarak' : jaraknya1, 'kelompok' : 0})

  for jarak2 in sekolah:
    nama2 = jarak2['namaSekolah']
    jaraknya2 = math.sqrt((((jarak2['X1'] - cluster2['X1'])**2) + ((jarak2['X2'] - cluster2['X2'])**2) + ((jarak2['X3'] - cluster2['X3'])**2) +((jarak2['X4'] - cluster2['X4'])**2) + ((jarak2['X5'] - cluster2['X5'])**2) + ((jarak2['X6'] - cluster2['X6'])**2)))
    jarakCluster2.append({'namaSekolah' : nama2, 'X1' : jarak2['X1'], 'X2' : jarak2['X2'],'X3' : jarak2['X3'],'X4' : jarak2['X4'],'X5' : jarak2['X5'],'X6' : jarak2['X6'], 'jarak' : jaraknya2, 'kelompok' : 0})

  for n in range(len(jarakCluster1)):
    a = cmp(jarakCluster1[n]['jarak'], jarakCluster2[n]['jarak'])
    if a == -1:
      jarakCluster1[n]['kelompok'] = 1
    elif a == 1:
      jarakCluster1[n]['kelompok'] = 2
    elif a == 0:
      jarakCluster1[n]['kelompok'] = 0
  
  for n in range(len(jarakCluster2)):
    a = cmp(jarakCluster2[n]['jarak'], jarakCluster1[n]['jarak'])
    if a == -1:
      jarakCluster2[n]['kelompok'] = 2
    elif a == 1:
      jarakCluster2[n]['kelompok'] = 1
    elif a == 0:
      jarakCluster2[n]['kelompok'] = 0

  for x in range(len(jarakCluster1)):
    if jarakCluster1[x]['kelompok'] == 1:
      c1 += 1
    elif jarakCluster1[x]['kelompok'] == 2:
      c2 += 1

  pusatbaru_c1 = []
  ex1_c1 = 0
  ex2_c1 = 0
  ex3_c1 = 0
  ex4_c1 = 0
  ex5_c1 = 0
  ex6_c1 = 0

  pusatbaru_c2 = []
  ex1_c2 = 0
  ex2_c2 = 0
  ex3_c2 = 0
  ex4_c2 = 0
  ex5_c2 = 0
  ex6_c2 = 0

  for data in jarakCluster1:
    if data['kelompok'] == 1:
      ex1_c1 += data['X1']
      ex2_c1 += data['X2']
      ex3_c1 += data['X3']
      ex4_c1 += data['X4']
      ex5_c1 += data['X5']
      ex6_c1 += data['X6']

    elif data['kelompok'] == 2:
      ex1_c2 += data['X1']
      ex2_c2 += data['X2']
      ex3_c2 += data['X3']
      ex4_c2 += data['X4']
      ex5_c2 += data['X5']
      ex6_c2 += data['X6']
  
  cluster1 = {'X1' : ex1_c1/c1,'X2' : ex2_c1/c1,'X3' : ex3_c1/c1,'X4' : ex4_c1/c1,'X5' : ex5_c1/c1,'X6' : ex6_c1/c1,}

  cluster2 = {'X1' : ex1_c2/c2,'X2' : ex2_c2/c2,'X3' : ex3_c2/c2,'X4' : ex4_c2/c2,'X5' : ex5_c2/c2,'X6' : ex6_c2/c2,}

  
  c_cluster1Awal = c_cluster1Akhir
  c_cluster2Awal = c_cluster2Akhir
  c_cluster1Akhir = c1
  c_cluster2Akhir = c2

  # print(c_cluster1Akhir, " & " , c_cluster2Akhir)

# pprint(jarakCluster1)
# pprint(jarakCluster2)

anggotaC1 = []
anggotaC2 = []
  
for datas in jarakCluster1:
  if datas['kelompok'] == 1:
    anggotaC1.append(datas)
  elif datas['kelompok'] == 2:
    anggotaC2.append(datas)

# pprint(anggotaC1)
# pprint(anggotaC2)

# MOORA

# menentukan bobot
bc1 = 0.25 #guru
bc2 = 0.2 #r.kelas
bc3 = 0.2 #r.lab
bc4 = 0.2 #r.perpus
bc5 = 0.15 #rasio pd:rb
bc6 = 0.25 #rasio guru:rb

#normalisasi cluster 1
normalized1 = []

sqrtC1 = 0
sqrtC2 = 0
sqrtC3 = 0
sqrtC4 = 0
sqrtC5 = 0
sqrtC6 = 0

for datas in anggotaC1:
  sqrtC1 += datas['X1']**2
  sqrtC2 += datas['X2']**2
  sqrtC3 += datas['X3']**2
  sqrtC4 += datas['X4']**2
  sqrtC5 += datas['X5']**2
  sqrtC6 += datas['X6']**2  

for dataku in anggotaC1:
  c1 = dataku['X1'] / math.sqrt(sqrtC1)
  c2 = dataku['X2'] / math.sqrt(sqrtC2)
  c3 = dataku['X3'] / math.sqrt(sqrtC3)
  c4 = dataku['X4'] / math.sqrt(sqrtC4)
  c5 = dataku['X5'] / math.sqrt(sqrtC5)
  c6 = dataku['X6'] / math.sqrt(sqrtC6)

  alternatif = {'namaSekolah' : dataku['namaSekolah'], 'C1' : c1,'C2' : c2,'C3' : c3,'C4' : c4,'C5' : c5,'C6' : c6,}
  normalized1.append(alternatif)

# pprint(normalized1)

# matrix terbobot
terbobot1 = []

for data in normalized1:
  c1 = data['C1'] * bc1
  c2 = data['C2'] * bc2
  c3 = data['C3'] * bc3
  c4 = data['C4'] * bc4
  c5 = data['C5'] * bc5
  c6 = data['C6'] * bc6

  alternatif = {'namaSekolah' : data['namaSekolah'], 'C1' : c1,'C2' : c2,'C3' : c3,'C4' : c4,'C5' : c5,'C6' : c6,}
  terbobot1.append(alternatif)

# pprint(terbobot1)

# nilai optimasi

for data in terbobot1:
  dMax = data['C1'] + data['C2'] + data['C3'] + data['C4'] + data['C6']
  dMin = data['C5'] 

  Yi = dMax - dMin
  data['Yi'] = Yi

def myFun(e):
  return e['Yi']

terbobot1.sort(reverse=True, key=myFun)

pprint(terbobot1)