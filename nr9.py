def find_sum(l):
    # ég skil að þetta er skilaverkefni en ég myndi alltaf not sum(__iterable) í staðin ef þetta væri mitt verkefni.
    r = 0
    for i in l:
        r += i
    return r

def find_number_of_elements(l):
    # auðvelda leiðin
    # return len(l)

    # erfiða leiðin
    c = 0
    for i in l:
        c += 1
    return c

def find_list_average(l):
    t = 0
    c = 0
    for i in l:
        c += 1
        t += i
    return t / c

def main():
    my_list = list()
    max_range = 5

    list_sum = 0
    number_of_elements = 0
    list_average = 0
    
    for i in range(0, max_range):
        num = int(input("Sláðu inn heiltölu á bilinu 1 til 100: "))
        my_list.append(num)
    
    list_sum = find_sum(my_list)
    number_of_elements = find_number_of_elements(my_list)
    list_average = find_list_average(my_list)

    print(f'Summa: {list_sum}\nFjöldi staka: {number_of_elements}\nMeðaltal: {list_average}')


if __name__ == '__main__':
    main()