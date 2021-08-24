def task_pow(base, power):
    if power == 2:
        return base * base
    if power % 2:
        return base * task_pow(base, power - 1)
    return task_pow(task_pow(base, power // 2), 2)


while True:
    print(task_pow(int(input('base: ')), int(input('power: '))))
