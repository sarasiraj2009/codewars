def likes(names):
    #your code here
    if len(names) == 0:
        like = "no one likes this"
    elif len(names)== 1:
        like = names[0] + " likes this"
    elif len(names)== 2:
        like = names[0] + " and " + names[1] + " like this"
    elif len(names)== 3: 
        like = names[0] + " , " + names[1] + " and " + names[2] + " like this"
    else:
        like = names[0] + " , " + names[1] + " and " + str(len(names)-2) + " others like this"
    return like


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
        