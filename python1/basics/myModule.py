def greeting(name: str = 'f'):
    print("Hello, " + name)


def kebab(name):
    print(name)


g = {'x': 2, 'y': 3}
z = {key: value*2 for key, value in g.items() if value == 2}
print(z)
a = [1, 2, 3]
b = [print(x, y) for y in a for x in a]
print(b)
# t = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4]]
# print(t)

print('__name__', __name__)
if __name__ == '__main__':
    greeting(name='jaja')
    greeting('eylon')
    greeting()
