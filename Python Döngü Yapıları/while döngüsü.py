"""Kullanıcı girisi programı"""

sys_kullanıcı_adı = "burhan"
sys_parola = "12345"
giris_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı :")
    parola = input("Parola :")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalıdır...")
        giris_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola Hatalıdır...")
        giris_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalıdır...")
        giris_hakkı -= 1
    else:
        print("Başarılı Giriş Yaptınız...")
        break

    if (giris_hakkı == 0):
        print("Giriş Hakkınız Bitmiştir.")
        break