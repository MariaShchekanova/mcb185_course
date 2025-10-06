for i in range (1, 100):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif (i % 3 == 0) and (i % 5 == 0):
        print ('FizzBuzz')
    else:
        print(i)

'''
def calculator (n):
    total = 0
    for i in range (1, n+1):
        total += i
    return total
'''


'''
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
'''


'''
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci_sequence(10)
'''


'''
def find_pythagorean_triples(limit=100):
    for a in range(1, limit):
        for b in range(a, limit):  
            c = (a**2 + b**2) ** 0.5
            if c % 1 == 0:  
                print(f"{a}, {b}, {int(c)}")

find_pythagorean_triples()
'''