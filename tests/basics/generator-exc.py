# Test proper handling of exceptions within generator across yield
def gen():
    try:
        yield 1
        raise ValueError
    except ValueError:
        print("Caught")
    yield 2

for i in gen():
    print(i)


# Test throwing exceptions out of generator
def gen2():
    yield 1
    raise ValueError
    yield 2
    yield 3

g = gen2()
print(next(g))
try:
    print(next(g))
except ValueError:
    print("ValueError")

try:
    print(next(g))
except StopIteration:
    print("StopIteration")
