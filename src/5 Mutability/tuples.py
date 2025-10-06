tuple1 = (3, 4, 5, 6, 7)
tuple2 = 6, 7, 8, 9
print(tuple1)
print(tuple2)


def test(a=1, b=[]):
    a += 1
    b.append(a)
    print(a)
    print(len(b))
    print()


test()
test()
test()
test()
