# İlk iki Fibonacci sayısını tanımla
a, b = 1, 2
total = 0

# 4 milyonun altındaki Fibonacci sayıları üret
while b < 4000000:
    # Eğer Fibonacci sayısı çiftse, toplama ekle
    if b % 2 == 0:
        total += b
    # Fibonacci dizisini güncelle
    a, b = b, a + b

# Sonucu yazdır
print(total)