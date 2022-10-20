num=int(input("Sisesta aasta: "))

div=400
div2=4
div3=100

if num%div == 0 or num%div2 == 0 and num%div3 != 0:

    print("On liig aasta")
else:
    print("Ei ole liig aasta")  