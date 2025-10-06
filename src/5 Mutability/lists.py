def main():
    suits = ["a", "b", "c"]
    suits2 = suits
    suits3 = suits.copy()
    suits.pop()
    suits.remove("a")
    suits.append("d")
    suits.extend(["e", "f"])
    print(suits)
    print(suits2)
    print(suits3)


if __name__ == "__main__":
    main()
