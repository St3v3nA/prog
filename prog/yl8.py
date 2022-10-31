num=int(input("Sisesta aasta: "))

n=400
n2=4
n3=100

if num%n == 0 or num%n2 == 0 and num%n3 != 0:
    print("On liigaasta")
else:
    print("Ei ole liigaasta")  