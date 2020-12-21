def merger(first_list, second_list):
    if first_list > second_list:
        count = 0
        count_el = len(first_list) - len(second_list)
        while count < count_el:
            second_list.append(None)
            count += 1
    return dict(zip(first_list, second_list))


print(merger([1, 2, 3, 4, 5, 6], [1, 2, 3, 4]))
