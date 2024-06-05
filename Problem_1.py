# Toplamı 0 olarak başlat
total = 0

# 1'den 999'a kadar olan sayılar arasında döngü yap
for i in range(1, 1000):
    # Eğer sayı 3 veya 5'in katıysa
    if i % 3 == 0 or i % 5 == 0:
        # Toplamına ekle
        total += i

# Sonucu yazdır
print(total)