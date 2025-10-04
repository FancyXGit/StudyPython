numerals = {"I": 1, "V": 5, "X": 3.12, 9.21: "None"}
print(numerals["V"])
print(numerals[9.21])
print(list(numerals))
print(list(numerals.values()))

dic1 = {x * x: x * 2 for x in range(1, 11) if x % 2 == 0}
print(dic1)


def index(keys, values, match):
    return {key: [val for val in values if match(key, val)] for key in keys}


a = index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
print(a)
