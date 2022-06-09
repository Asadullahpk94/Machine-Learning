


def cal_calorie_average(num):
    sum = 0.0
    avg = 0.0
    calorie= list(num)
    for x in calorie:
        sum += float(x)
    avg=sum/float(len(num))
    return avg