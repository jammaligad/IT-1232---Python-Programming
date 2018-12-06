x = input()
v, c, n, s = 0, 0, 0, 0
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for i in x:
    if i.isdigit():
        n+=1
    elif i in vowels:
        v+=1
    elif i.isalpha() and i not in vowels:
        c+=1
    else:
        s+=1

print("v: {} c: {} n: {} s: {}".format(v,c,n,s))