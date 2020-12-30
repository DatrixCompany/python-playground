def default_check_cons(b=3, a=[]):
    return [a, b]


def1 = default_check_cons()
def2 = default_check_cons()
print(def1, def2)
def1[0].append(2)
def1[1] = 444
print(def1, def2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
