a = int(input("Sisesta number vahemikus 1-9: ")) 

n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )

print (n1+n2+n3)