#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

print("Boy ve Kilo İndeksi")

boy = (input("Boyunuzu Giriniz: "))
kilo = (input("Kilonuzu Giriniz: "))
boy = float(boy)
kilo = float(kilo)

bki = (kilo/((boy/100)**2))

print(bki)


if bki <= 18.5:
    print("Zayıf")
elif bki > 18.5  and bki  <= 25:
    print("Normal")
elif bki > 25 and bki   <= 30:
    print("Kilolu")
elif bki > 30:
    print("Obez")





