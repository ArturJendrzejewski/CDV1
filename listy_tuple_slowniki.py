#listy
progr=['PHP','Python']
print(type(progr))
progr.append('C#')
print(progr)
count=progr.count('PHP')
print(f'PHP wystepuje {count} razy\n')

#tuple
name=('Krystyna', 'Anna')
print(name)
print(type(name))
first=name[0]
print(first)

#name.append('Janusz')

#slowniki

person={
    'name': 'Anna',
    'surname': 'Nowak'
}

print(person)
print(type(person))
print(person['name'])
print(person.keys())
print(person.get('height','brak danych'))

person['height']=178
print(person.get('height','brak danych'))

names={
    'Imię1': input("Podaj imię 1 :"),
    'Imię2': input("Podaj imię 2 :"),
    'Imię3': input("Podaj imię 3 :")
}

for key in names.keys():
    print(key, ':', names[key])