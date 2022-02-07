def months(iso):
    if isinstance(iso, str) == False:
        return None
        
    s = iso.lower()
    m = {
        "is": ["janúar", "febrúar", "mars", "apríl", "maí", "júní", "júlí", "ágúst", "september", "október", "nóvember", "desember"],
        "en": ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "jp": ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    }
    
    if s in m:
        return m[s]
    else:
        return None

def main():
    print(months('IS'))
    print(months('EN'))
    print(months('DE'))
    print(months('ES'))
    print(months('JP'))
    print(months('EU'))

if __name__ == '__main__':
    main()