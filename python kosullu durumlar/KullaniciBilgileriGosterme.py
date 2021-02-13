#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

print("Kullanıcının girdiği değerler:")

ad=input ("Adınızı giriniz lütfen: ")

soyad=input ("Soyadınızı giriniz lütfen: ")

numara=input ("Numaranızı giriniz lütfen: ")

numara= int(numara)



degerler =[ad,soyad,numara]

print("Adınız: {}\nSoyadınız: {}\nNumaranız : {}".format(degerler[0],degerler[1],degerler[2]))

print("Adınız","Soyadınız","Numaranız", "Kaydediliyor......")
