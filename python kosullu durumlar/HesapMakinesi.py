print("""*********************
Hesap Makinesi Programı
İşlemler: 

1: Toplama 

2: Çıkarma

3: Çarpma

4: Bölme


********************
""")

a = int(input("Birinci Sayı:"))

b = int(input("İkinci Sayı:"))

islem = input("İşlem Giriniz:")

if islem =="1":
    print("{} ile {} 'ın toplamı {} 'dır".format(a,b,a+b))

elif islem == "2":
    print("{} ile {} 'nın farkı {} 'dır".format(a, b, a-b))

elif islem == "3":
    print("{} ile {} 'ın çarpımı {} 'dır".format(a, b, a * b))

elif islem == "4":
    print("{} ile {} 'ye bölümü {} 'dır".format(a, b, a / b))

else:
    print("Yanlış İşlem Girdiniz")





