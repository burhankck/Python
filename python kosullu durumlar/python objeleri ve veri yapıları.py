#!/usr/bin/env python
# coding: utf-8

# In[1]:


3+4


# In[2]:


3-4


# In[3]:


3*4


# In[4]:


4*4*4


# In[5]:


56/7


# In[6]:


2.1+4.2


# In[7]:


2.5-4.2


# In[8]:


2.4*4.2


# In[9]:


54.25/7.1


# In[10]:


2+4+4-5


# In[11]:


kocak = 10


# In[12]:


kocak


# In[13]:


kocak = 15


# In[14]:


15


# In[15]:


kocak


# In[16]:


kocak =3.4


# In[17]:


kocak


# In[18]:


kocak * kocak * kocak 


# a=4
# b=3
# c=a+2*b
# c

# In[23]:


3kocak = 5 


# In[24]:


kocak_=5


# In[25]:


kocak_


# In[26]:


pi_sayısı =3.14
cap=4
cevre=pi_sayısı*cap
cevre


# In[27]:


a =4
b =3


# In[28]:


a


# In[29]:


b


# In[30]:


a,b =b,a


# In[31]:


a


# In[32]:


b


# In[48]:


i = 5 


# In[34]:


i


# In[35]:


i =i+1


# In[36]:


i


# In[37]:


i+=1


# In[38]:


i


# In[39]:


i+=2


# In[40]:


i


# In[41]:


b =3 
b *=4 


# In[42]:


b


# In[44]:


#tamsayı bölme (//)
a = 345 
b = 36 
a/b 


# In[45]:


a//b


# In[46]:


22.7 / 11.4 


# In[47]:


22.7 // 11.4


# In[48]:


#kalan bulma (%)
13%4


# In[49]:


22.7 % 11.4 


# In[50]:


4 % 2


# In[51]:


#üs bulma  soluna yazdıgımız sayı soluna yazdıgımız sayının kuvvetini alıyor , karakök bulmayı sağlayabilir (**) 
2**4


# In[52]:


3**9


# In[53]:


#karakök bulma 
64**0.5


# In[54]:


25**0.5


# In[55]:


8 ** (1/3)


# In[56]:


#işaret degistirme (-)
a = -4
-a


# In[ ]:


# işlem sırası (parantez içi her zaman önce yapılır, carpma bölme toplama cıkarmadan önce yapılır,işlemler soldan sağa
değerlendirilir)


# In[ ]:


#string oluşturma tek tırnak 
'kocak'
#cift tırnak 
"kocak"
#üc tırnak 
"""kocak"""


# In[ ]:


#tırnaklar nasıl koyulmalıdır 
'Burhan'ın bugün dersi var. #yanlış
"Burhan'ın bugün dersi var. " #doğru 
'Burhan\'ın bugün dersi var.'#doğru ters / bitiş tırnağı değil demektir. Kaçış dizisi deniyor bunlara.


# In[58]:


#stringi index ile parcalama ; stringler birer karakter dizileri oldukları için her bir karakterin içinde yeri vardır. örnegin 
# ali kelimesinin a l i yerleri index olarak adlandırılır. bu dil ve cogu dilde indexler genelde (0) dan başlar. 
# [ ] bu şekil ile gösterilir. 
a= 'burhan'
a


# In[59]:


a[3]


# In[60]:


a[5]


# In[ ]:


a='merhaba'


# In[62]:


#stringler baştan olduğu gibi sondan da indexlenebiliyorlar. sondan -1,-2 şeklinde gider.
b="kocak"
b[-1]


# In[63]:


b[-3]


# In[69]:


s="Python Programlama Dili"
#Peki uzun bir stringin sadece belirli bir kısmını almak istiyoruz ne yapmalıyız.bunun için [] ve : işaretlerini kullancaz.
#[baslama indeksi : bitis indeksi : atlama degeri]


# In[70]:


s[4:10]


# In[71]:


#baslangıc değeri belirtmemişsen en baştan baslayarak alır.
s[:10]


# In[72]:


#bitis değeri belirtmemissen en sonuna kadar alır.
s[8:]


# In[73]:


#iki değeri belirtmemişse tüm stringi al.
s[:]


# In[75]:


#son karaktere kadar al.(son karakter -1 den basladıgı icin)
s[:-1]


# In[77]:


#atlama degeri veriyoruz sadece örnekte iki iki atlayarak gidiyor birini alıyor değerin birini almıyor.
s[::2]


# In[78]:


s[::3]


# In[79]:


s[4:12:2]


# In[80]:


s[::-1] 
#stringi tersten yazılıyor. 


# In[81]:


# bir stringin uzunlugunu nasıl buluruz ? bunun icin len() fonksiyonu vardır 
m ="merhaba"
len(m)


# In[82]:


#direk olarak stringi degistiremezsin.
q="burhan"


# In[31]:


q[3]='t'


# In[84]:


#pythonda stringler aynı sayılar gibi birbirleriyle toplanabılıyor.
a='python'
b='programlama'
c='dili'
a+b+c


# In[85]:


'python' * 3


# In[86]:


#stringler degistirilmiyor demistik ama bu işlemi yaparsak yok oluyor python bu işlemi en baştan yapıyor.Bu sekide degistiriliyor
n="burhan"
n= n +"kocak"


# In[87]:


n


# In[1]:


#Veri tipi dönüşümleri
#Tam sayıyı ondalıklı sayıya çevirme float fonksiyonunu kullanıyoruz
a = 43 
a =float(a)
a


# In[2]:


#Ondalıklı sayıyı tam sayıya çevirme int fonksiyonu kullanıyoruz
b= 3.14
b=int (b)
b


# In[50]:


#Stringleri sayıya çevirme str fonksiyonu kullanıyoruz
str(345)
v =str(345)
len(v)
#doğru çalışıyor yukarıdaki kodlardan dolayı sorun yaşanıyor.


# In[1]:


n = "3232323232"
int(n)


# In[6]:


m = 3.45
p=float(m)
p


# In[9]:


#hatalı kod 
o="3.45.21"
y=float(o)
y


# In[11]:


#Print fonksiyonu ve formatlama
#print ()
"murat"
#Bu şekilde print fonksiyonu olmadan olabilir fakat projeleri dosyalara yazacağımız için kodu çalıştırınca hataya yol açabilir
#Bu yüzden print fonksiyonu gereklidir
#İçine değer veririz ve ekrana yazar.


# In[12]:


print(3.14)


# In[13]:


print("burhankck")


# In[14]:


a = 4
b =16
print(a+b)


# In[15]:


#print fonksiyonunda aynı anda bir kaç değer  bastırmak istersek virgülle ayırmamız lazım.
print(35,4.12,"merhaba","burhan")


# In[17]:


#stringlerde özel bazı karakterler en çok kullanılan karakterler 
#\ln karakteri alt satıra ekrana yazdırma işlemidir.
#\t karakteri bir tab boşluk bırakarak yazdırma işlemidir.
print("merhaba\nburhan\nkocak\n")


# In[18]:


print("merhaba       iyi misin")
#bunu yapmak yerine aşağı bakalım.


# In[19]:


print("ocak\tsubat\t\tmart")


# In[20]:


print("a\t\t\t\tb")


# In[21]:


#type() fonsksiyonu içine gönderilen değerin hangi veri tipinde olduğunu söyler.
type(34)


# In[22]:


type("burhan")


# In[23]:


type(3.15)


# In[24]:


#Print fonksiyonu özellikleri ve parametreleri
#pyhton'da araya boşluk bırakılarak yazılıyor bildiğinize göre ama bu sep parametresi kullanarak istediğimi karakterleri 
#kullanabiliyoruz
print(3,4,5,6,7,8,9)


# In[27]:


#sep parametresi sayesinde değerler arasında nokta koyuluyor.
print(3,4,5,6,7,8,9, sep=".")


# In[28]:


#değerler arasına / sembolu yerleştiriliyor 
print(15,10,2020,sep="/")


# In[29]:


#Yıldızlı parametreler 
print("python")


# In[30]:


# her bir karakterin arasına boşluk koyularak yazılır (*) parametresinde.
print(*"python ")


# In[31]:


print("T","B","M","M", sep=".")


# In[34]:


print(*"TBMM",sep=".")
#Daha kısa şekilde yıldız yardımıyla yapabiliriz.


# In[35]:


#Stringlerde formatlama ve biçimlendirme 
#Burada üç tane süslü parantezimiz ([{}]) var  bunların yerine sırasıyla format fonksiyonu içindeki değerler geçiyor.
"{},{},{}".format(3.21,4.5131,6.32411454)


# In[36]:


a = 3 
b = 4
print("{} + {}'nın toplamı {}'dir".format(a,b,a+b))


# In[38]:


#Süslü parantezin içindeki sayılar format fonksiyonu içindeki hangi değerin geleceğini söylüyor.
"{1} {2} {0}".format("burhan",12,94)


# In[42]:


#Süslü parantezin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğini söylüyor
"{:.2f} {:.1f} {:.2f}".format(3.134,54.32,32.1)


# In[2]:


#Liste veri tipleri 
#stringler degistirilemez ama listeler degistirilebilir karakterlerdir.
#liste olusturma, parçalama ve indeksleme, temel liste metodları ve işlemleri, iç içe listeler 
#listelerin içine istediğin veri tipini koyabilirsin
liste=["elma",35,"merhaba",18.2]
type(liste)


# In[5]:


liste = []
liste


# In[6]:


liste2=[1,2,3,4,5,6,"burhan"]
len(liste2)


# In[9]:


#stringi listeye çevirmek için 
liste3= list("merhaba")
liste3


# In[11]:


len(liste3)


# In[14]:


liste4=[1,2,3,4,"burhan","kocak"]

liste4[2]


# In[15]:


liste4[5]


# In[16]:


liste4[-1]


# In[17]:


len(liste4)


# In[18]:


liste4[len(liste4)-1]


# In[19]:


#liste parçalama işlemleri
liste4[:4]


# In[20]:


liste4[:5]


# In[21]:


liste4[::2]


# In[22]:


liste4[::-1]


# In[28]:


#Temel liste metodları ve işlemleri : Listeler stringler gibi birbirleriyle toplanıyorlar başka bir degiskene atanabiliyorlar
liste5 =[2,3,4]
liste6 =[5,6,7]
liste7=liste5 + liste6
liste7


# In[29]:


liste5 * 2


# In[30]:


#şuan liste5 yeni değeri hala bu değil 2,3,4 olarak devam ediyor bunun için yeni değer olarak atmamız lazım  
liste5= liste5 * 2
liste5


# In[31]:


#listeler direk olarak degistirilir demistik stringlerde yapılamıyordu.
a = "burhan"
a[1] =p


# In[32]:


liste6


# In[34]:


liste6[1] = 9
liste6


# In[37]:


#listeyi 2.ci sıradakine kadar degistir yeni değer atıyoruz.
liste6[:2]= [10,12]
liste6


# In[39]:


#Methodlar : Bir çok veri tipinin üzerinde uygulanabilen değisik islemler gerçeklestirebilen fonksiyonlar anlamına gelir.
#Listenin methodlarına erismek icin liste. diyip method adını çekiyoruz.

liste8=[2,4,5,6,7]
liste8


# In[45]:


#liste.append fonksiyonu listeye yeni bir eleman ekliyor.(sonuna)
liste8.append("10")
liste8


# In[46]:


#liste.pop fonksiyonu listeye son elemanını çıkarır atar.
liste8.pop()


# In[47]:


liste8


# In[48]:


liste8.pop(0)


# In[49]:


liste8


# In[53]:


#sort methodu : Bu method sırası bozuk olan değerleri büyükten kücüge doğru sıralar.
liste9 =[1,4,76,8,3,21,67,43]
liste9.sort()
liste9


# In[57]:


liste10=["c","python","html","css","photoshop"]
liste10.sort()
liste10


# In[59]:


#reverse =true kodu listeyi bu sefer tam tersinden sıralama yapar büyükten kücüge değilde kücükten büyüge
liste10.sort(reverse =True)
liste10


# In[60]:


liste11=[1,2,3,4,5,67,7,8,]

liste11[50]
#böyle bir indeks yok liste11'in içinde hata veriyor.


# In[62]:


#iç içe listeler : Listenin içinde başka bir listeyide barındırabiliriz.
liste12=[[1,2],[3,4],[5,8]]
liste12


# In[64]:


#Demetler (Tuplelar):Listelere oldukça benzer fakat demetler değistirilemez. Programın icinde degistirilmesini istemediğimiz
#değerler varsa bunu demetlerin içine depolayıp  atabiliriz.
demet=(1,2,3,4,5,6)
type(demet)
#type tipini soruyoruz.


# In[65]:


demet[4]


# In[66]:


demet[-1]


# In[67]:


demet[0]


# In[68]:


demet[:4]


# In[69]:


demet[::-1]
#demeti ters ceviriyoruz.


# In[71]:


#demetlerin iki tane fonksiyonu vardır.
#demet.count fonksiyonu  değeri demetin içindeki o değerden kaç tane var onu söyler bize 
demet2=[1,1,1,1,2,2,3,3,4,4,5,7,]
demet2.count(1)


# In[72]:


demet2.count(2)


# In[74]:


#olmayan bişeyi yapalım 0 tane olarak göstericek yani içinde o değer hiç yok.
demet2.count(9)


# In[77]:


#demet.indeks fonksiyonu herhangi bir değerin eğer içinde var ise nerede olduğunu söylüyor.(indeksi söylüyor)
demet3=[1,2,3,4,5,6,7,87,8]
demet3.index(3)


# In[78]:


demet3.index(87)


# In[85]:


#demetler degistirilemez 
demet4 = (1,2,3,4)
demet4[2] =10
demet4


# In[ ]:


#demetler listelere göre daha az kullanıyorlar. programda degistirilmesi istemediğiniz değerler varsa bunu demetlerin içine
#atabilirsiniz. Demetler çok daha az listelere göre daha hızlıdır.


# In[ ]:


#Sözlüker:Aynı gerçek hayattaki sözlük gibi davranan veri tipidir.Her bir eleman anahtar değer iliskisine sahip oluyor.


# In[86]:


sözlük1 = {"bir":1,"iki":2,"üç":3,"dört":4}
type(sözlük1)


# In[88]:


sözlük2={}
sözlük2


# In[90]:


sözlük=dict()
sözlük


# In[103]:


sözlük3={"beş":5,"altı":6,"yedi":7,"sekiz":8}
sözlük3


# In[104]:


#sözlükteki anahtarı girerek değerleri çağırıyoruz.
sözlük3["altı"]


# In[105]:


sözlük3["yedi"]


# In[106]:


sözlük3["on"]
#hata veriyor on çünkü değerler içinde yok.


# In[107]:


#sözlüğe on sayısını ekliyeceğiz şimdi.
sözlük3["on"]= 10
sözlük3
#nereye eklediği önemli değil çünkü indexlere erişmiyoruz.


# In[111]:


a ={"bir":[1,2,3,4],"iki":[[6,7],[9,8],[10,11]],"üç":15}
a


# In[114]:


a["bir"]


# In[113]:


a["üç"]


# In[115]:


a["iki"]


# In[116]:


a["iki"][1]


# In[117]:


a["iki"][1][0]


# In[119]:


#sözlükteki elemanın değerini degistirmek istersek.
sözlük3


# In[120]:


sözlük3["beş"]=18
sözlük3


# In[122]:


#sözlükteki değeri artırıyoruz.
sözlük3["beş"] += 2
sözlük3
#beşteki değer iki artmıştır.


# In[ ]:


#sözlükler degistirilebiliyor dinamik olarak eleman eklenebiliyor.


# In[123]:


#sözlüklerin temel methodları :Sadece anahtarları almak istiyorsak keys fonksiyonu veriyor.
sözlük3


# In[125]:


sözlük3.keys()
#sadece anahtarları aldık.


# In[126]:


#values değeride tam tersine sözlükteki değerleri alıyor.
sözlük3.values()


# In[128]:


#anahtarlar hangi değere karşılık geliyorsa onları gösteriyor direk.
sözlük3.items()


# In[129]:


#Kullanıcan girdi alma  input()  fonksiyonu inputu calıstırdıgımız zaman bizden bir girdi bekler input.
input()


# In[1]:


#inputun içine parametre verelim.
input("Lütfen sayı girin:")


# In[4]:


x = input("Lütfen sayı gir:")
print("Kullanıcının girdiği değer",x)


# In[5]:


a= input("Lütfen sayı gir:")
print(a*3) 
#bunun nedeni şu şekilde inputtan dönen değer hep string yazı olarak geliyor.Veri tipi dönüşümü lazım.


# In[6]:


a= input("Lütfen sayı gir:")
print(type(a))
#Bakın hep string şekilde geliyor input değerimiz bunu bizim değiştirmemiz lazım int ile ve nasıl yaparız ?


# In[7]:


a =int(input("Lütfen sayı gir:"))
print(a*3)
#Bakın bu şekilde int olarak tanımladık değeri ve kodumuz doğru bir şekilde çalıştı.


# In[13]:


a =int(input("Lütfen birinci sayıyı gir:"))
b =int(input("Lütfen ikinci sayıyı gir:"))
c =int(input("Lütfen üçüncü sayıyı gir:"))
print("toplamları",a+b+c)


# In[14]:


a =int(input("a:"))
print(a)
#böyle bir (a) değeri girerse kullanıcı programda hata verecektir.
#stringin tam sayısa dönüsmesi icin her  karakterin rakam olması gerekiyor. 
#ilerde göreceğiz ama kullanıcıya hata verdirebiliriz böyle bir durumda.


# In[5]:


say1 = 10
say2 = 20
say1,say2 = say2,say1
say1


# In[ ]:




