for i in range(1000, 3001):

    a = i // 1000
    b = (i // 100) % 10
    c = (i // 10) % 10
    d = i % 10

    if a % 2 == 0:
        if b % 2 == 0:
            if c % 2 == 0:
                if d % 2 == 0:
                    print(i, end=" ")