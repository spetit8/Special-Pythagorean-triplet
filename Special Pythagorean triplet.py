a = 0
A = 0
B = 0
C = 0

def FindABC():
    for c in range(1000, 3, -1):
        C = c
        for b in range(c, 2, -1):
            B = b
            a = 1000 - b - c
            if a ** 2 + b ** 2 == c ** 2 and a > 0:
                return print(a * b * c)

FindABC()
