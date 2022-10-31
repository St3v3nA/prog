name = input("Sisesta oma nimi: ")

print("Tere " ,name,)

elukoht = input("Kus sa elad?: ")

if elukoht.lower() == 'saaremaa':
    print("Saaremaa on parim saar")

age = int(input("Sisesta oma vanus: "))

if age < 18:
    print("Olete liiga noor, et autot juhtida")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul!")
elif age > 18:
    print("Te võite autot juhtida")