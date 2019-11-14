# Fibonacci.py

def fibs():
    fibs = [1,2]

    for i in range(1,9):
        f = fibs[i-1] + fibs[i]
        fibs.append(f)

    return fibs
