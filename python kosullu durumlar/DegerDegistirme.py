#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

print("Kullanıcıdan İki sayı giriniz")

say1 = int(input("Birinci sayıyı giriniz: "))
say2 = int(input("İkinci sayıyı giriniz: "))

sayılar=[say1,say2]


say1,say2 = say2,say1


print("Birinci sayı: {}\nİkinci sayı: {}\n".format(sayılar[0],sayılar[1]))


print("Sayılar yazdırılıyor...")

print("Birinci sayı: {}\nİkinci sayı: {}\n".format(sayılar[1],sayılar[0]))












