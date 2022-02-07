from math import factorial

def list_factorial(s):
    # geyma niðurstöður
    r = []
    for i in s:
        # ef stak er utan 2-10 
        if i > 10 or i < 2:
            return -1
        # ef stak er inní leyfðum mörkum
        else:
            # reikna með factorial falli úr 'math' og bæta í niðurstöður
            r.append(factorial(i))
    # skila niðurstöðum
    return r

def main():
    print(list_factorial([2, 5, 7, 10]))

if __name__ == '__main__':
    main()