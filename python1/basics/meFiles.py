f = open('text.txt')
g = f.read()
f.close()
print(g)

f2 = open('writeFile.txt', "a")
f2.write('\npsyyyyy')
f2.close()
