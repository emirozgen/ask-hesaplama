isim1 = input("Adınız:")
isim2 = input("Eşinizin adı:")

ask = len(isim1) + len(isim2)

if len(isim1) > len(isim2):
    ask -= 5

else:
    ask += 3
ask *= 42
ask = ask / (100 + len(isim2))

ask = 10 if ask > 10 else round(ask, 0)

print("{} ve {} skorunuz {} dır 10 üzerinden".format(isim1, isim2, ask))