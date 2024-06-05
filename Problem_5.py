import math

def lcm(a, b):
    # İki sayının en küçük ortak katını (EKOK) hesapla
    return a * b // math.gcd(a, b)  # EKOK = (a * b) / EBOB

result = 1  # Sonucu başlat

# 1'den 20'ye kadar olan sayılar arasında döngü
for i in range(1, 21):
    result = lcm(result, i)  # Her sayı için EKOK hesapla ve güncelle

print(result)  # Sonucu yazdır