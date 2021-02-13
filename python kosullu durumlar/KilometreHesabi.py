#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini
# alın ve  sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.


print("Sayın müşterimiz yakıtınız hesaplanacaktır:")

km =  (input("Kilometrede ne kadar yaktığınızın  değerinizi giriniz:"))
km = float(km)
yol= int (input(" Kaç kilometre yol gittiğinizin değerini giriniz:"))

hesaplama = [km,yol]

degerler = (km*yol)


print("Ne kadar yaktığınızı giriniz: {}\nNe kadar yol yaptığınızı giriniz: {}\n".format(hesaplama[0],hesaplama[1]))

print("Sayın müşterimiz toplam ödemeniz gereken miktar:",km*yol)