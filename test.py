import datetime
import random
from 排序算法.冒泡排序 import bubble_sort

# print("result", bubble_sort(array))   final is in  0:00:00.077850



if __name__ == '__main__':
    array = [random.randint(0, 999) for i in range(999)]  # 随机数列
    random.shuffle(array)
    print("array ", len(array), array)
    # 开始时间
    start = datetime.datetime.now()

    print("result", bubble_sort(array))

    # 结束时间
    end = datetime.datetime.now()
    # 输出
    print("final is in ", end - start)

