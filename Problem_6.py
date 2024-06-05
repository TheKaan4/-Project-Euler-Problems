# İlk 100 doğal sayının karelerinin toplamını hesapla
sum_of_squares = sum(i**2 for i in range(1, 101))

# İlk 100 doğal sayının toplamını hesapla ve karesini al
square_of_sum = sum(range(1, 101)) ** 2

# Karesi alınmış toplam ile karelerinin toplamı arasındaki farkı yazdır
print(square_of_sum - sum_of_squares)