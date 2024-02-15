import datetime

now     = datetime.datetime.now()
banyak  = []
nama    = []
harga   = []
jumlah  = []
kode    = []


print ("=====================================")
print ("            BURGER BINGIR            ")
print ("=============== Menu ================")
print ("1. Burger Spesial          Rp. 25.000")
print ("2. Burger Istimewa         Rp. 20.000")
print ("3. Burger Biasa            Rp. 15.000")
print ("4. Burger Biasa banget     Rp. 10.000")
print ("=====================================")


print ('\n')
print ("Output masukannya sebagai berikut")
kasir = input ("Nama Kasir      : ")
pesan = int (input ("data Makanan    : "))


for i in range(pesan):
  print ("data makanan ke-",i+1)
  kode.append (int(input ("kode makanan    : ")))
  banyak.append (int (input ("jumlah beli     : ")))


  if kode[i] == 1:
    nama.append("Burger Spesial")
    harga.append("25.000")
    jumlah.append(banyak[i]*int(25000))

  elif kode[i] == 2:
    nama.append("Burger Istimewa")
    harga.append("20.000")
    jumlah.append(banyak[i]*int(20000))

  elif kode[i] == 3:
    nama.append("Burger Biasa")
    harga.append("15.000")
    jumlah.append(banyak[i]*int(15000))

  elif kode[i] == 4:
    nama.append("Burger Biasa Banget")
    harga.append("10.000")
    jumlah.append(banyak[i]*int(10000))

  else:
    nama.append("-")
    harga.append("0")
    jumlah.append(banyak[i]*int(0))


hasil = sum(jumlah)
akhir = sum(banyak)
if akhir >= 5:
  pajak = hasil * 0.1
  bayar = hasil + pajak
  print ("Total Bayar     : ",bayar)
  print ("Jumlah Total    : ",akhir)
else:
  pajak = "-"
  bayar = hasil
  print ("Total Bayar     : ",bayar)
  print ("Jumlah Total    : ",akhir)


uang = int (input ("uang pembayaran : "))
cs   = str (input ("nama pembeli    : "))
kembalian = uang - bayar
print ("Kembalian       : ",kembalian)
print ('\n')

print ("Output keluarannya sebagai Berikut")
print ("---------------------------------------")
print ("             BURGER BINGIR             ")
print ("---------------------------------------")
print ("kasir    : ", kasir)
print ("Customer : ", cs)
print ("Waktu    : ", now)
print ("--------------------------------------")
for i in range(pesan):
  print (banyak[i] , nama[i] , harga[i])
print ("--------------------------------------")
print ("SubTotal :", hasil)
print ("Pajak    :", pajak)
print ("Total    :", bayar)
print ("--------------------------------------")
print ("Bayar    :", uang)
print ("Kembali  :", kembalian)
print ("--------------------------------------")
print ("------------ Terima kasih ------------")

