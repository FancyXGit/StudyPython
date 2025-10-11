class Account:
    interest = 0.02

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


tom = Account("tom", 100000)
jim = Account("Jim", 1)

print(tom.interest)

# print()
# jim.interest = 0.01
# print(tom.interest)
# print(jim.interest)

print()
Account.interest = 0.005
print(tom.interest)
print(jim.interest)
