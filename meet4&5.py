# Input dari user
# aritmatika 

# Belajar Inputan
rizal = input ("masukkan kata : ")
print ("isi dari rizal : ", rizal,"bertipe data :", type (rizal)) 

# belajar aritmatika dasar 
x = 11.5
y = 4

# penjumlahan +
hasil = x + y
print ("x + y =", hasil )

# pengurangan -
hasil = x - y
print ("x - y =", hasil )

# perkalian x
hasil = x * y 
print ("x * y =", hasil )

# pembagian /
hasil = x / y
print ("x / y =", hasil )

# perpangkatan exponen **
hasil = x ** y
print ("x ^ Y =", hasil )

# modulus %
hasil = y % X
print (" x mod y =", hasil )

# floor division (pembulatan kabawah) //
hasil = x // y
print ("x // y =", hasil )

# aritmatika prioritas
# (), exponen, perkalian/pembagian, penjumlahan/pengurangan
x = 3
y = 4
z = 5

hasil = ( x ** y * (z + x) / y - z % x // y)
print(hasil)