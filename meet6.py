# MACAM MACAM PERBANDINGAN 
# lebih besar >
# lebih kecil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# tidak sama dengan !=
# sama "is" ==
# tidak sama "is not" !=


x = 4
y = 5

# lebih besar >
hasil = x > y
print(x, '>', y, 'adalah', hasil)

# kebih kecil <
hasil = x < y
print(x, '<', y, 'adalah', hasil)

# lebih besar sama dengan >=
hasil = x >= y
print(x, '>=', y, 'adalah', hasil)

# lebih kecil sama dengan <=
hasil = x <= y
print(x, '<=', y, 'adalah', hasil)

# tidak sama dengan!=
hasil = x != y
print(x, '!=', y, 'adalah', hasil)

# sama dengan "is" ==
hasil = x is y
print(x, 'is', y, 'adalah', hasil)

# tidak sama "is not" !=
hasil = x is not y
print(x, 'is not', y, 'adalah', hasil)

# > < >= <= == != ini adalah perbandingan literal
# x = 4, 4 = perbandingan literal
# x is 4 (tidak bisa, karena yang di bandingkan adalah lietral)
# x is y ( bisa, karena yang dibandingkan adalah objact)