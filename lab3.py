#zad1
def numbers(n: int) -> None:
        if n < 0:
            return
        else:
            print(n)
        numbers(n-1)


numbers(10)
print("----------------")
#zad2

def fib(n: int)->int:
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))
print("----------------")

#zad3

def power(number: int, n: int):
    if n==0:
        return 1
    else:
        return (number*power(number, n-1))

print(power(7,7))

#zad4

def reverse(txt: str):
    if len(txt) == 0:
        return txt
    else:
       return reverse(txt[1:])+txt[0]

print(reverse("nike"))

#zad5

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n*(factorial(n-1))

print(factorial(5))

#zad 6

def prime(n: int, i=2) -> bool:
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime(n,i+1)

print(prime(10))

#zad 7
def n_sums(liczby: int, lista=[]):
    if liczby > 1000:
        return lista
    temp = [int(x) for x in str(liczby)]
    print(temp)
    if sum(temp[::2]) == sum(temp[1::2]):
        lista.append(liczby)
    return n_sums(liczby + 1, lista)
print(n_sums(5))

