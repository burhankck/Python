#!/usr/bin/env python
# coding: utf-8

# In[2]:


#mantıksal değerler (boolean) veri tipi iki değere sahip oluyorlar bir koşulun doğru yada yanlıs oldugunu kontrol ediyor.
# true yada false şeklinde oluyor. büyük harfle yazılır baş harfi yoksa hata verir.
a= True
type(a)


# In[3]:


b = False
type(b)


# In[4]:


bool(14)


# In[5]:


bool(-1)


# In[6]:


bool(3.14)


# In[7]:


#bool değeri sadece 0'a eşitse false şeklinde verir görelim.
bool(0)


# In[8]:


bool(0.0)


# In[9]:


1 == 1


# In[10]:


1 == 2


# In[12]:


#Eğer bir degisken değerini sonradan atamak istiyorsanız geçici olarak (None) atanmamış şeklinde yapabilirsiniz.
a =None 
#herhangi bir veri tipi olmuyor belirlemedik cünkü
a = 4
a


# In[ ]:


#KARSILASTIRMA OPERATÖRLERİ 
"""
== İki değer birbirine eşitse True değilse False değerini verir.

!= İki değer birbirine eşit degilse True, Diğer durumda True döner.

> Soldaki değer sağdaki değerden büyükse True değil ise False döner.

< Soldaki değer sağdaki değerden küçük ise True değil ise False döner.

>= Soldaki değer sağdaki değerden büyük veya eşit ise True değil ise False döner.

<= Sağdaki değer soldaki değerden büyük veya eşit ise True değil ise False döner.

"""


# In[13]:


"burhan" =="burhan"


# In[16]:


"burhan" == "kocak"


# In[17]:


"burhan" != "kocak"


# In[18]:


"burhan" != "burhan"


# In[19]:


2<4


# In[20]:


2>4


# In[1]:


"Araba" > "Zulam"
#A harfi daha önce oldugu icin daha kücük olarak algılıyor program 


# In[3]:


"Zulam" > "Araba"
#Z harfi sonradan geldiği icin daha büyük gibi algılıyor program 


# In[4]:


3<=4


# In[5]:


2.4<=1.4


# In[ ]:


#MANTIKSAL BAGLACLAR
#Daha çok karsılastırma işlemi yapıldığı zaman bunları kullanırız.

#and operatörü : Tüm işlemlerin True olması lazım Bir tane bile yanlış çıkarsa False olarak karşımıza çıkar.


# In[6]:


1<2


# In[8]:


"burhan" == "burhan"


# In[9]:


1<2 and "burhan"=="burhan"


# In[10]:


1>2 and "burhan"=="burhan"


# In[14]:


#or operatörü : Genel sonucun True cıkması icin hergangi bir işlem True olması yeterli. 
#False çıkması için hepsinin False çıkması lazım 

1>2


# In[12]:


"burhan" == "burhan"


# In[15]:


1>2 or  "burhan"=="burhan"
#Bir false Bir true oldugu icin sonuc True cıktı demiştik ki bir tane True olması yetiyor sonucun True olması için.


# In[16]:


3>5


# In[17]:


"burhan"=="kocak"


# In[18]:


3>5 or "burhan"=="kocak"
#hepsi False olduğu icin false cıktı cevap.


# In[19]:


# not operatörü : True ise False yapıyor. False ise True yapıyor başka yaptıgı bişey yok.
2 == 2


# In[20]:


not 2 == 2


# In[21]:


"burhan" =="burhan"


# In[22]:


not "burhan"=="burhan"


# In[23]:


5>10


# In[24]:


not 5>10


# In[26]:


not (2.14 > 3.20 or ( 2!=2 and "burhan"=="burhan"))
#kafamız karısıyor ise parantez icine alarak tek tek yapabiliriz bu durumlarda sonuc True.


# In[ ]:




