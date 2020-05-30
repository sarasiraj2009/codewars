def to_jaden_case(string):
    s = string.split()
    l = len(s)

    for n in range(l):
        s[n] = s[n].capitalize()
    
    string =(" ".join(s))
    
    return string
