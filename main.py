import time

Sayaç = int(input("Zamanı saniye cinsinden giriniz:"))


for x in range(Sayaç,0,-1):
    saniye = x % 60
    dakika = int(x / 60) % 60
    saat = int(x / 3600) % 24
    print(f"{saat:02}:{dakika:02}:{saniye:02}")
    time.sleep(1)

print("Zaman bitti.")
