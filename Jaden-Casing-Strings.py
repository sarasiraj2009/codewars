def to_jaden_case(string):
    #my code 
    s = string.split()

    for n in range(len(s)):
        s[n] = s[n].capitalize()
    
    string =(" ".join(s))
    
    return string
