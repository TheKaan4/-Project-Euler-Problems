def largest_prime_factor(n):
    # 2'den başlayarak asal çarpanları kontrol et
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

print(largest_prime_factor(600851475143))