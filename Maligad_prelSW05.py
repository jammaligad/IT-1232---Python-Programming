x, vowels, y  = input().lower(), ['a','e','i','o','u'], []
for i in x: 
    if i in vowels and i not in y: y.append(i)
print(y)