"""Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. """

sayi= int (input("Bir sayı giriniz :"))
sum = 0

for   i in  range(1,sayi):
    if (sayi % i == 0):
        sum += i
        print("{} Sayıya bölünüyor...".format(i))

if (sum == sayi):
    print("{} Sayı mükemmel sayıdır...".format(sayi))
else:
    print("Sayı mükemmel sayı değildir...".format(sayi))






