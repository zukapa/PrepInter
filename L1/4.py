def deposit(amount, period):
    min_amount = {'begin_sum': 1000, 'end_sum': 10000, '6': 5, '12': 6, '24': 5}
    mid_amount = {'begin_sum': 10000, 'end_sum': 100000, '6': 6, '12': 7, '24': 6.5}
    max_amount = {'begin_sum': 100000, 'end_sum': 1000000, '6': 7, '12': 8, '24': 7.5}
    if min_amount['begin_sum'] <= amount < min_amount['end_sum']:
        return check(amount, min_amount, period)
    if mid_amount['begin_sum'] <= amount < mid_amount['end_sum']:
        return check(amount, mid_amount, period)
    if max_amount['begin_sum'] <= amount < max_amount['end_sum']:
        return check(amount, max_amount, period)


def check(amount, type_amount, period):
    if period == 6:
        return calc_dep_not_cap(amount, period, type_amount['6'])
    if period == 12:
        return calc_dep_not_cap(amount, period, type_amount['12'])
    if period == 24:
        return calc_dep_not_cap(amount, period, type_amount['24'])


def calc_dep_not_cap(amount, period, percent):  # функция подразумевает выплату процентов раз в год
    period = period / 12
    count = 0
    calculate = amount
    while count < period:
        if period < 1:
            calculate += amount / 100 * (percent * period)
            count += 1
        else:
            calculate += amount / 100 * percent
            count += 1
    return calculate


def calc_dep_cap(amount, period, percent):  # функция подразумевает выплату процентов раз в год
    period = period / 12
    count = 0
    calculate = amount
    while count < period:
        if period < 1:
            calculate += amount / 100 * (percent * period)
            count += 1
        else:
            calculate += calculate / 100 * percent
            count += 1
    return calculate


print(deposit(10000, 24))
