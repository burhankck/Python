#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

print("En büyük sayıyı yazdıran program :")

a = int(input("Birinci sayıyı giriniz: "))

b = int(input("İkinci sayıyı giriniz: "))

c = int(input("Üçüncü sayıyı giriniz: "))



if a > b and a > c:
    print(" Birinci sayı en büyük sayıdır")
elif b > a and b > c:
    print("İkinci sayı  en büyük sayıdır")
elif c > a and c > b:
    print(" Üçüncü sayı en büyük sayıdır ")
else:
    print("Geçersiz Sayı Girdiniz: ")
