x, y = [], []
x += input().split(" ")
for word in x:
    if x.count(word) < 2: y.append(word)
print(y)
