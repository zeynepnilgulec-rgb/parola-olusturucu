import random

karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk= int(input("Parola uzunlugunu giriniz:"))

parola = ""

for i in range(uzunluk):
    secilen = random.choice(karakterler)
    parola += secilen

print("olusturulan parola:",parola)
