#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# İf bloğu 

#18 yaş engeli

yas =int(input("Yaşınızı giriniz:"))
if yas<18:
    print("Mekana Giremezsiniz")
if yas>=18:
    print("Mekana Girebilirsiniz")
    
    


# In[ ]:


# Veya if Blogunun yanına Else bloğu kullanabiliriz Else = Değilse demek.
#18 yaş engeli

yas =int(input("Yaşınızı giriniz:"))
if yas<18:
    print("Mekana Giremezsiniz")
else:
    print("Mekana Girebilirsiniz")
    


# In[ ]:


sayı = int(input("Sayı giriniz:"))
if sayı<0:
    print("Negatiftir")
else: 
    print("Pozitiftir")
    


# In[ ]:


# IF- ELİF -ELSE BLOKLARI
#bir durum birden cok kosula baglı olabiliyor bu yüzden if elif else bloklarını kullanmalıyız.


# In[5]:


islem = input("İşlem Giriniz")

if islem == "1":
    print("İşlem 1 Seçildi:")
elif islem=="2":
    print("İşlem 2 Seçildi:")
elif islem=="3":
    print("İşlem 3 Seçildi:")
elif islem=="4":
    print("İşlem 4  Seçildi:")
else:
    print("Geçersiz İşlem:")
    


# In[13]:


note = float(input("Notunuzu Giriniz:"))

if (note >= 90):
    print("AA")
elif (note >= 85):
    print("AB")
elif (note >= 80):
    print("BB")
elif (note >= 75):
    print("CB")
elif (note >= 70):
    print("CC")
elif (note >= 65):
    print("CD")
elif (note >= 60):
    print("DD")
else:
    print("Dersten Kaldınız: ")
    
        
    
        
        
    

    
    


# In[14]:


note = float(input("Notunuzu Giriniz:"))

if (note >= 90):
    print("AA")
if (note >= 85):
    print("AB")
if (note >= 80):
    print("BB")
if (note >= 75):
    print("CB")
if (note >= 70):
    print("CC")
if (note >= 65):
    print("CD")
if (note >= 60):
    print("DD")
else:
    print("Dersten Kaldınız: ")
    
#Bu sekilde sadece if ile yaparsak 4 tane işlem geldi sebebi elif blogu sadece yukardaki islem saglanmadıgı zaman çalışır.
# if blokları ama yukardaki islem sağlansada sağlanmasada çalışıyor o yüzden 4 tane sonuc verdi bize.
#elif ve else yukardaki durumun sağlanmadıgı zaman calısan durumlardır.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




