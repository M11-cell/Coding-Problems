


def fermats_theorem(a, b, c, n):
    
    if n <= 2 or a <= 0 or b <= 0 or c <=0:
        return "Invalid Inputs"
    
    if a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work"

if __name__ == '__main__':
    msg = fermats_theorem(1, 3, 2, 3)
    print(msg)