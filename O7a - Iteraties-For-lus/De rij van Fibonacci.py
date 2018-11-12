#input
n = int(input('getal n: '))

#bewerking
if n == 0:
    antw = '0'
elif n == 1 or n == 2:
    antw = '1'
else:
    def fib(n):
        a, b = 1, 1
        for _ in range(n-1):
            a, b = b, a + b
        return a
    antw = fib(n)

#antwoord
print(antw)