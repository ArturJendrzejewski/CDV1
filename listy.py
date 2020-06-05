progr=['Python', 'PHP','C#','JS','Java']
print(progr)
print(type(progr))

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)

#dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie elementów
conutElement=progr.count('Python')
print(conutElement)

#ilosc elementów w liscie
countElementsOfList=len(progr)
print(countElementsOfList)

#polazenie list
anotherList=['C','C++']
progr.extend(anotherList)
print('progr'+str(progr))
print('anotherList'+str(anotherList))

#usuwanie elemetnów z listy
new=progr
print('New list: '+str(new))
new.clear()
print('New list: '+str(new))
print('Rozmiar New list: '+str(len(new)))
print('progr list'+ str(progr))
print('Rozmiar progr: '+str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x)
print(y)

country=['Polska','Czechy','Egipt','Turcja','USA']
countryAdd=[input('Dodaj Element do listy :')]
country.extend(countryAdd)
countryAdd=[input('Dodaj Element do listy :')]
country.extend(countryAdd)
opcja=input("1) Wyświetl pierwsze 3 elementy listy\n2) Wyświetl elementy listy, które dodałem\n3) Wyświetl zawartość listy\n4) Wyczyść zawartość listy\n5) Znajdź element w liście\nWybór :")
if int(opcja)==1:
    opcja1=country[0:3]
    print(opcja1)
    print(country)
elif int(opcja)==2:
    opcja2=country[-2:]
    print(opcja2)
    print(country)
elif int(opcja)==3:
    print(country)
elif int(opcja)==4:
    country.clear()
    print(country)
elif int(opcja)==5:
    opcja5=str(input("Podaj :"))
    if opcja5 in country:
            print("twoje dane znajdują się w country")
    else:
            print("twoje dane nie znjadują sie w country")
    print(country)