# a, b, ve c'nin toplamı 1000 olacak şekilde a ve b'yi bulmak için döngü
for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b  # c'yi toplamdan çıkarak hesapla
        # Eğer a, b ve c bir Pisagor üçlüsü oluşturuyorsa
        if a * a + b * b == c * c:
            print(a * b * c)  # a, b ve c'nin çarpımını yazdır
            break  # Bir çözüm bulduktan sonra döngüden çık