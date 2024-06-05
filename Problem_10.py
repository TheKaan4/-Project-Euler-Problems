def sieve(limit):
    # Asallıkları belirlemek için bir dizi oluştur
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 ve 1 asal değildir
    for i in range(2, int(limit**0.5) + 1):  # n'nin kareköküne kadar kontrol et
        if is_prime[i]:  # Eğer i asalsa
            for j in range(i*i, limit, i):  # i'nin katlarını asal olarak işaretle
                is_prime[j] = False
    # Tüm asal sayıları bir liste olarak döndür
    return [x for x in range(limit) if is_prime[x]]

primes = sieve(2000000)  # 2 milyona kadar olan asal sayıları bul
print(sum(primes))  # Asal sayıların toplamını yazdır