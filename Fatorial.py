def fatorial(n,show):
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'\033[35m{i}\033[m', end=' ')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5,show=True))
