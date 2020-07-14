import datetime
import random

def query_sort(array):
    if len(array) < 2:
        return array  # 最多只有一个元素的数组就别来凑热闹了
    else:
        p = array[0]
        l = [i for i in array[1:] if i <= p]
        g = [i for i in array[1:] if i > p]
        return query_sort(l) + [p] + query_sort(g)


array = [i for i in range(0, 200, 3)]  # 随机数列
random.shuffle(array)
print("array ", len(array), array)   # [0, 3, 6, 9, 12, 15, 18]
# 开始时间
start = datetime.datetime.now()

res = query_sort(array)
# 结束时间
end = datetime.datetime.now()
# 输出
print("result", res)
print("final is in ", end - start)

