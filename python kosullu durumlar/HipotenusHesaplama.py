#Kullanıcıdan bir dik üçgenin dik olan
# iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

a = int(input("Dik olan birinci kenar uzunluğunu giriniz: "))

b = int(input("Dik olan ikinci kenar uzunluğunu giriniz: "))



c = (a**2 + b**2) **0.5



degerler = [a**2,b**2,c]

print("Birinci sayı: {}\nİkinci sayı: {}\n".format(degerler[0],degerler[1],degerler[2]))

print("Hesaplanıyor...", c)
print("Hipotenüs karesi",c**2)
