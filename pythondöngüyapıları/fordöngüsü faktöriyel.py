print("""***Faktöriyel Bulma Programı 

Çıkmak için q harfine basınız***""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program Sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i
        print("Faktoriyel",faktoriyel)


