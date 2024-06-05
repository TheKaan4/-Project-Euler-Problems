def is_palindrome(n):
    # Sayıyı stringe çevir ve tersini alarak palindrom olup olmadığını kontrol et
    return str(n) == str(n)[::-1]

max_palindrome = 0  # En büyük palindromu saklamak için değişken

# 100'den 999'a kadar olan sayılar arasında çift döngü
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j  # Sayıların çarpımını hesapla
        # Eğer çarpım palindromik ve şu ana kadarki en büyük palindromdan büyükse
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product  # En büyük palindromu güncelle

print(max_palindrome)  # Sonucu yazdır