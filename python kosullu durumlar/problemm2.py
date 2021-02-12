#Kullanıcıdan aldığınız boy ve kilo değerlerini bulan beden kitle endeksi bulan program.

print("Vücut kitle endeksi")

a = int(input("Boyunuzu Giriniz:"))
b = int(input("Kilonuzu Giriniz:"))

degerler = [a,b]
Vücutendeksi = ((a**2)/b)

print("Vücut endeksi hesaplanıyor...")

print("Boyunuzu giriniz: {}\nKilonuzu giriniz: {}\n".format(degerler[0],degerler[1]))

print("Vücüt endeksi hesaplanıyor...",(a**2/b))