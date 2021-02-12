print("""
ATM makinesine hoşgeldiniz
işlemler;
1. bakiye sorgulama
2. para yatırma 
3. para cekme
programdan cıkmak icin q harfine basınız.""")


bakiye = 1000

while True:
    islem = input("İşlemi seçiniz :")
    if (islem == "q"):
        print("Yine Bekleriz...")
        break
    elif (islem =="1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))

    elif (islem =="2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar

    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if (bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz..")
            continue
            bakiye -= miktar
    else:
        print("Geçersiz işlem...")
