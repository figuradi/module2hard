import random
def window():
    window_first = []
    value_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for i in value_1:
        i = random.choice(value_1)
        window_first.append(i)
        break
    pwd = []
    value_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for j in value_2:
        for k in value_2:
            if i % (j + k) == 0 and k > j:
                pwd.append(str(j) + str(k))


    print('В первом окне выпало:', window_first)
    print('Значит пароль: ', ' '.join(pwd))

window()