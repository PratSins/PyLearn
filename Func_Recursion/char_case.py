def up_low(s):
    d = {'upper':0, 'lower':0}
    
    for ch in s:
        if ch.isupper():
            d['upper'] += 1
        elif ch.islower():
            d['lower'] += 1
        else:
            pass

    print(f"\nOriginal String --> {s}")
    print(f'Lowercase count: {d["lower"]}')
    print(f'Uppercase count: {d["upper"]}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
