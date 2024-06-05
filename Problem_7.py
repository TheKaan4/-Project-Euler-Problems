def is_prime(n):
    if n <= 1:  # 1 veya daha küçük sayılar asal değildir
        return False
    if n <= 3:  # 2 ve 3 asaldır
        return True
    if n % 2 == 0 or n % 3 == 0:  # 2 veya 3'e bölünen sayılar asal değildir
        return False
    i = 5
    while i * i <= n:  # n'nin kareköküne kadar kontrol et
        if n % i == 0 or n % (i + 2) == 0:  # 6k ± 1 kuralını kullan
            return False
        i += 6
    return True

count = 0  # Asal sayıları saymak için sayaç
num = 1  # Asal sayıları bulmak için başlangıç noktası

while count < 10001:  # 10001. asal sayıya ulaşana kadar döngü
    num += 1  # Sayıyı arttır
    if is_prime(num):  # Eğer sayı asal ise
        count += 1  # Asal sayıyı say

print(num)  # 10001. asal sayıyı yazdır