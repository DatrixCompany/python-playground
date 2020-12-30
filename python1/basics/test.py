from myModule import greeting as greet, kebab as kababa
import datetime

list = ['a', 'b', 'c']
ans = 'a' in list
print(ans)

greet('dany')
kababa(datetime.datetime.now().year)


class Test():
    def __init__(self, attr=[]):
        self.attr = attr


a = Test()
b = Test()
a.attr.append(1)
print(a.attr, b.attr)


class Test2():
    def __init__(self, attr=None):
        self.attr = attr if attr is not None else []


a = Test2()
b = Test2()
a.attr.append(1)
print(a.attr, b.attr)


g = [1]
print(g) if (g) else print('h')

g = ([5], 6, 5)
f = ([5], 6, 5)
k = [1]
s = [1]
print(g == f)
print(k == s)
k.append(2)
print(k == s)


def default_check_cons(b=3, a=[]):
    return [a, b]


def1 = default_check_cons(b=3)
def2 = default_check_cons(b=3)
print(def1, def2)
def1[0].append(2)
def1[1] = 444
print(def1, def2)
