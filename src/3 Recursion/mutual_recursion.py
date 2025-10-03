def split(n):
    return n // 10, n % 10


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    two_times_last = last * 2
    luhn_digit = two_times_last // 10 + two_times_last % 10
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


print(luhn_sum(5105105105105100))
