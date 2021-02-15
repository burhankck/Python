#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# in operatörü istediğimiz değerin liste içinde olup olmadığını kontrol ediyoruz.
5 in[1,2,3,4]


# In[4]:


"p" in "python"


# In[5]:


"s" in "python"


# In[6]:


4 in (1,2,3)


# In[7]:


not 4 in (1,2,3)


# In[8]:


# FOR  döngüsü listelerin demetlerin stringlerin ve hatta sözlüklerin üstünde gezinmemizi sağlıyor.
liste = [1,2,3,4,5,6,7]
for eleman in liste:
    print(eleman)


# In[12]:


toplam = 0
liste = [1,2,3,4,5,6,7]
for eleman in liste:
 toplam = toplam + eleman
 print("Toplam : {} Eleman : {}".format(toplam,eleman))
print(toplam)


# In[13]:


54 % 2


# In[16]:


#çift sayıyı bulalım liste içinde.
liste1 = [1,2,3,14,53,24,76,11]
for eleman1 in liste1:
    if eleman1 % 2 == 0:
     print(eleman1)


# In[21]:


x = "Python"
for i in x:
    print(i)


# In[22]:


x = "Python"
for i in x:
    print(i*3)


# In[25]:


demet = (1,2,3,4,)
for a in demet:
    print(a)


# In[27]:


# demetlerle ilgili for döngünüsünde pratikler bulunuyor bakalım.
liste2 = [(1,2),(3,4),(5,6),(7,8)]
for b in liste2:
    print(b)


# In[29]:


# her döngünde 1 ve 2 değerlerini ayrı ayrı almak istiyorum bunun klasik bir yöntemi vardır bakalım.
for (i,j) in liste2:
    print("i : {} j : {}".format(i,j))


# In[31]:


liste3 = [(1,2,3),(4,5,7),(8,9,10)]
for (x,y,z) in liste3:
    print("x : {} y : {} z : {}".format(x,y,z))


# In[32]:


liste3 = [(1,2,3),(4,5,7),(8,9,10)]
for (x,y,z) in liste3:
    print(x*y+z)


# In[33]:


sözlük = {"bir":1, "iki":2, "üç":3, "dört":4}
sözlük.keys()


# In[34]:


sözlük.values()


# In[35]:


sözlük.items()


# In[36]:


sözlük = {"bir":1, "iki":2, "üç":3, "dört":4}
for eleman in sözlük:
    print(eleman)


# In[38]:


for eleman in sözlük.values():
    print(eleman)


# In[39]:


for eleman in sözlük.items():
    print(eleman)


# In[40]:


sözlük.items()


# In[42]:


for i,j in sözlük.items():
    print("Anahtar:",i, "Değer:",j)


# In[46]:


# while DÖNGÜSÜ belirli bir koşul sağlandığı sürece bloğunda işlemleri gerçekleştirmeye devam eder.Sona ermesi için koşul
# durumunun bir süre sonra FALSE olması gereklidir.
# Döngüde i değerlerini ekrana yazdırma örneğine bakalım.
i = 0
while(i<10):
    print("i'nin değeri:",i)
    i = i + 1


# In[47]:


i = 0
while(i<20):
    print("i'nin değeri:",i)
    i = i + 2


# In[48]:


a = 0
while(a<40):
    print("Python Öğreniyorum...")
    a = a + 1


# In[51]:


liste = [1,2,3,4,5]
for i in liste:
    print(i)


# In[52]:


# while döngüsünde index = index +1 seklinde kendimiz arttırmamız lazım ama for döngüsünde bunu kendisi yapıyor unutursak eğer
# while döngüsü sonsuza girer ve hatalara yol açar.
index = 0
while(index < len(liste)):
    print("index:",index, "Liste ELemanı:",liste[index])
    index = index + 1 


# In[53]:


#range() FONKSİYONU bu yapı baslangıc ve bitis opsiyonel olarak artırma değeri alarak listelere benzeyen sayı dizisi olusturur.
range (0,20)


# In[55]:


print("range")


# In[56]:


print(*range(0,20))


# In[57]:


print(*range(0,100))
# böyle birseyi elimizle yazmak çok zaman alır ama range fonksiyonu ile cok daha kolay yapılabiliyor.


# In[58]:


print(*range(0,20))


# In[59]:


print(*range(15))


# In[61]:


print(*range(0,15))
# bir üstteki ile aynıdır. 0'ı koymasakta olur Gösterim amaçlı.


# In[62]:


print(*range(1,100,2))


# In[63]:


print(*range(1,100,3))


# In[64]:


print(*range(5,100,5))


# In[65]:


print(*range(20,0))
#böyle yapınca hic bisey olusturmuyor. Hep yukarı dogru gittiği icin sonlanıyor 21'e gitmeye calısıyor aslında ama son değer
# 20 olduğu icin hic bir islem yapmıyor kodu calıstırınca.


# In[66]:


print(*range(20,0,-1))
# -1 atlayarak git dersek sondan başa doğru bu sekilde gelebilir.


# In[67]:


liste = [1,2,3,4,5,6]
for i in liste:
    print(i)


# In[68]:


for i in range(1,101):
    print(i)


# In[1]:


for i in range(10):
    print("*" * i)


# In[ ]:


# döngülerde kullanılan ifadeler break ve continue
# BREAK İFADESİ Sadece ve sadece içinde bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa en içteki döngüde 
# break kullanışmışsa sadece içteki döngü sona erer.
# SUANKI DÖNGÜMÜZÜ BİLİYORUZ ;


# In[2]:


b = 0 
while(b < 10):
    print(b)
    b = b + 1


# In[3]:


b = 0 
while(b < 10):
    if (b == 5):
        break
    print(b)
    b = b + 1


# In[4]:


liste = [1,2,3,4,5]
for i in liste:
    print(i)


# In[7]:


liste = [1,2,3,4,5]
for i in liste:
    if (i ==3):
        break
    print("i:", i)


# In[ ]:


#örnek: kullanıcı ismini söylesin ismini bastıralım sürekli kullanıcı q harfine basınca sonlandırsın.
#while true : sonlandırma ifadesi kullanılmamıssa sonsuza kadar gidiyor.
#break kullanılmıssa ama bir yerde sonlanacak demektir.


# In[21]:


while True:
    isim = input("İsim(Cıkmak icin 'q' harfine basınız):")
    if (isim == "q"):
        print("Programdan cıkılıyor..")
        break
        print("İsminiz :",isim)
# görüldüğü gibi break ile while döngünüsünü sonlandırdık break böyle kullanılıyor.


# In[8]:


# continue ifadesi break'e göre çok az kullanılıyor.
# döngü herhangi bir yerde continue ifadesi ile karsılasıyorsa geri kalan islemleri yapmadan direk blogun basına döner.
liste5 = [1,2,3,4,5,6,7,8,9,10]
for i in liste5:
    print("i:" ,i)


# In[4]:


liste6 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in liste6:
    if(i == 3 or i == 5 ):
        continue
    print(i)


# In[ ]:


i = 0 # Bu kodda sonsuz döngü olayı nedir ? Bu kodu calıstırmayalım. 
while (i<10):
    if (i == 2):
        continue
        print(i)
        i = i + 1
# Bu kodda i= 2 oldugunda sonsuz döngüye girecek continue bunu devam ettircek ve print(i) kısmına gecemeyip i'yi arttırmayacak
# bu yüzden sonsuz döngü olarak devam edecek simdi bunu düzeltelim.


# In[1]:


i = 0 
while (i<10):
    if (i == 2):
        i = i + 1 # Burayı bir artırırsak continue komutuna gelmeden kod calısır sonsuz döngüye girmemis olur.
        continue
    print(i)
    i = i + 1


# In[2]:


# LİST COMPREHENSİON :
# listelerdeki append metodunu hatırlayalım.
liste = [1,2,3]
liste.append(4)


# In[3]:


liste


# In[4]:


# her bir liste1 elemanını liste2 ye atacagız simdi. Ama uzun bir yöntem bunu list comprehension ile daha kolay yapacagız.
liste1 = [1,2,3,4,5]
liste2 = []
for i in liste1:
    liste2.append(i)
print(liste2)


# In[6]:


liste3 = [1,2,34,5,6,7,8]
liste4 = [i for i in liste3]
print(liste4)
# bu yöntem list comrehension yöntemidir.


# In[7]:


liste5 = [3,4,5,6]
liste6 =[i*2 for i in liste5]
print(liste6)


# In[9]:


liste1 = [(1,2),(3,4),(5,6)]
liste2 = [i*j for i,j in liste1]
liste2


# In[10]:


s = "Python"
liste1 = [i*3 for i in s]
print(liste1)


# In[22]:


liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]

for i in liste:
    for x in i:
        print(x)
       


# In[25]:


liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = list()
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)
       


# In[26]:


liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print(liste1)
# bu sekilde daha kısa kodlama ile yapabiliriz list comprehension ile.


# In[ ]:




