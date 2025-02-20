# Kullanıcıdan birinci sayıyı alıyoruz ve sayi1 adlı değişkene atıyorum
sayi1 = float(input("Birinci sayıyı girin: "))
# Kullanıcıdan ikinci sayıyı alıyoruz ve sayi2 adlı değişkene atıyorum
sayi2 = float(input("İkinci sayıyı girin: "))
#Toplama işlemi yapıyorum: sayi1 ve sayi2'yi topluyorum
toplam = sayi1 + sayi2
# Toplama işlemi sonucunu ekrana çıktı olarak veriyorum
print("Toplam", toplam)

#Çıkarma işlemi yapıyorum: sayi1'den ve sayi2'yi çıkarıyorum
çıkarma = sayi1 - sayi2 
# Çıkarma işlemi sonucunu ekrana çıktı olarak veriyorum
print("Çıkarma", çıkarma)

#Çarpma işlemi yapıyorum: sayi1 ile sayi2'yi çarpıyorum
çarpma = sayi1 * sayi2
# Çarpma işlemi sonucunu ekrana çıktı olarak veriyorum
print("Çarpma", çarpma)

#Bölme işlemi yapıyorum: sayi1'yi sayi2'ye bölüyorum
bölme = sayi1 // sayi2
# Bölme işlemi sonucunu ekrana çıktı olarak veriyorum
print("Bölme", bölme)

#Mod alma işlemi yapıyorum: sayi1'in sayi2'e bölümünden kalanı buluyorum
mod_alma = sayi1 % sayi2
# Mod alma işlemi sonucunu ekrana çıktı olarak veriyorum
print("Mod_alma", mod_alma)

#Üs alma işlemi yapıyorum: sayi1'in sayi2 üssünü alıyorum
üs_alma = sayi1 ** sayi2
# Üs alma işlemi sonucunu ekrana çıktı olarak veriyorum
print("Üs_alma", üs_alma)