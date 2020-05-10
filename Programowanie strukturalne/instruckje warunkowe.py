x=6

if x==5:
    print ("x jest rowna 5")
else:
    print("x nie jest rowny 5")
    print("x jest rowny: "+ str(x))

print("koniec instrukcji warunkowej")

######################################

y=False
if y==True:
    print("prawda")
else:
    print("fałsz")

#######################################

z=5>6
if z:
    print("prawda")
else:
    print("fałsz")

x=input("poraj x:")
y=input("podaj y:")
z=input("podaj z:")

if x>y and x>z:
    print("x jest najwiekszy")
elif y>x and y>z:
    print("y jest najwiekszy")
else:
    print("z jest najwiekszy")