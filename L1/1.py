def gen_table(first, second):
    first_string = [i for i in range(second + 1)]
    table = [first_string]
    count = 0
    while count < first:
        in_table = [first_string[count + 1]]
        for ind, val in enumerate(first_string):
            if ind == 0:
                continue
            else:
                in_table.append(in_table[0] * val)
        table.append(in_table)
        count += 1
    str_table = ''
    for i, v in enumerate(table):
        str_table += f'\n'
        for ind, val in enumerate(v):
            str_table += f'{val}\t'
    return str_table


print(gen_table(10, 10))
