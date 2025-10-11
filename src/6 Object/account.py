class account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def deposit(self, bill):
        self.balance += bill

    def withdraw(self, bill):
        self.balance -= bill

    def get_balance(self):
        return self.balance


def main():
    a = account("Yes", 19000)
    print(a.get_balance())
    print(a.get_name())
    a.withdraw(300)
    print(a.get_balance())
    a.deposit(400)
    print(a.get_balance())


if __name__ == "__main__":
    main()
