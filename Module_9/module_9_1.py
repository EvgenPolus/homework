

def apply_all_func(int_list, *functions):
    results = {}
    for funct in functions:
        f_name = funct.__name__
        date = funct(int_list)
        results.__setitem__(f_name, date)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))