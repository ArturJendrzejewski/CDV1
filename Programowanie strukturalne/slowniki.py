slownik={'key1':'value1','key2':'value2'}

pracownik={
    'name':'Anna',
    'surname':'Nowak',
    'city':'Poznań',
    'age':20,
    'namesChildren':['Tomasz','Krystyna'],
    'namesParents':['Paweł','Katarzyna']
}
print(pracownik)
print(pracownik['namesChildren'])
print(pracownik['namesChildren'][0])

pracownik['height']= 180
pracownik['weight']= 80
print(pracownik)

key='age'
if key in pracownik:
    del pracownik[key]
    print(f'klucz {key} został usunięty')
else:
    print(f'Klucz o nazwie {key} nie znaleziono w slowniku pracownik')
print(pracownik)

print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())

for key in pracownik.keys():
    print(key, ':', pracownik[key])