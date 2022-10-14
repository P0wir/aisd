#zadanie 1
# s1 = 'J'
# s2 = 'Kowalski'
# s = s1+'.'+s2
# print(s)

#zadanie 2
# s = "Jan"
# s2 = s[0]
# s3 = 'Kowalski'
# s4 = s2+'.'+s3
# print(s4)

#zadanie 3
# x = '20'
# y = '22'
# z = 21
#
# print(int(x+y)-z)

#zadanie 4

# def foo(x, y, z):
#     return int(x+y) - z
#
# imie = "Jan"
# s1 = imie[0]
# Nazwisko = "Kowalski"
#
# print(s1+'.'+Nazwisko, foo('20','22',57))

#zadanie 5

# def foo(x, y):
#     if x > 0 and y > 0 and y != 0:
#         return x/y
# print(foo(5,3))

#zadanie 6
# suma=0
# for i in range(0,1000):
#     suma += int(input("podaj liczbe"))
#     if suma < 100:
#         continue
#     break

#zadanie 7
# l = ["y","b","c","d"]
# print(l)
# def foo(x):
#     return tuple(x)
# print(foo(l))

#zadanie 8

#lista=[]
#for x in range(10):
#    a=input("element listy")
#    lista.append(a)
#krotka=tuple(y for y in lista)
#print(krotka)

#zadanie 9.

#def foo(x):
#    return{
#        1:'Poniedziałek',
#        2:'Wtorek',
#        3:'Środa',
#        4:'Czwartek',
#        5:'Piątek',
#        6:'Sobota',
#        7:'Niedziela',
#    }.get(x,'dzien tygodnia')
#print(foo(5))

#zadanie 10.

#def Palindrom(napis):
#    for x in range(int(len(napis)/2)):
#        if(napis[x]!=napis[(len(napis)-1)-x]):
#            return False
#    return True
#print(Palindrom('ala'))
















