banned_words = [
    "cogent",
    "cobent",
    "retn",
]

def check_word(w):
    if w.lower() in banned_words:
        return True
    else:
        return False

def list_adder_censored(l, e):
    if check_word(e):
        return "Staki ekki bætt í lista því það er bannorð!"
    else:
        if e in l:
            return "Staki ekki bætt í lista því það var í honum."
        else:
            l.append(e)
            return "Staki bætt í lista."

def main():
    x = ["lumen", "zayo", "telia"]
    print(list_adder_censored(x, 'lumen'))
    print(list_adder_censored(x, "cogent"))
    print(list_adder_censored(x, "gtt"))
    print(x)


if __name__ == '__main__':
    main()