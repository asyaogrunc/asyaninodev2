#Kullanıcıdan bir sayı alıp n sayıyı n değişkenine atıyorum
n = int(input("Bir sayı girin: "))
# Toplam değişkenini 0 olarak başlatıyorum
toplam = 0
# 1'den n'ye kadar olan sayıları döngü ile topluyorum
for i in range(1, n + 1): 
# Her bir sayıyı toplam değişkenine ekliyorum
    toplam += i
# Birden n'ye kadar olan sayıların toplamını ekrana çıktısını alıyorum
print("1'den", n, "ye kadar olan sayıların toplamı:", toplam)