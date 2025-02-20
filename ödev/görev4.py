# Kullanıcıdan bir metin alıyorum
metin = input("Bir metin girin: ")
# Ters çevrilmiş metni saklamak için boş bir string başlatıyorum
ters_metin = ""
# Kullanıcının girdiği metnin her bir karakteri üzerinde döngü başlatıyorum
for i in metin:
# Her bir karakteri başa ekleyerek ters çevirmeye başlıyorum
    ters_metin = i + ters_metin
# Ters çevrilmiş metnin ekrana çıktısını alıyorum
print("Ters metin:", ters_metin)