def list_adder(l, e):
    if e in l:
        return "Staki ekki bætt í lista því það var í honum."
    else:
        l.append(e)
        return "Staki bætt í lista."

def main():
    x = ["cogent", "zayo", "telia"]
    print(list_adder(x, "cogent"))
    print(list_adder(x, "gtt"))
    print(x)


if __name__ == '__main__':
    main()