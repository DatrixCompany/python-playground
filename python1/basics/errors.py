def g(x):
    assert x % 2 == 0, 'Error MSG'
    if (x % 3 == 0):
        raise AssertionError('Cant divide 6')
    return x / 2


try:
    print(g(5))
except AssertionError as err:
    print('no err msg')
    print(err)
finally:
    print('And then do something, failed or not...')

try:
    print(g(6))
except AssertionError as err:
    print(err)

try:
    print(g(8))
except AssertionError as err:
    print(err)
