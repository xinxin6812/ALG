import datetime

# 开始时间
start = datetime.datetime.now()

number = [i for i in range(0, 200, 3)]  # 随机数列
print("随机数列：", len(number), number)   # [0, 3, 6, 9, 12, 15, 18]
find = 39  # 目标搜寻 18
MAX = len(number)

def fib_loop(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

Fib = [fib_loop(i) for i in range(MAX)]  #  创建斐波那契数列
print("生成的斐波那契数列：", len(Fib), Fib)


def findx(n):  # 找X的值
    i = 0
    while Fib[i] <= n:
        i += 1
    i -= 1
    return i   # 找到第i个Fib元素小于等于MAX+1

def fibsearch(number, find, Fib):
    x = findx(find + 1)  # 斐波那契数列中第x个数刚好不大于find + 1。find是确定的，所以比较的起始点是确定的。
    m = MAX - Fib[x]  # 得到一个较小的差值。m的值也是确定的。
    print(f"x = {x}, m = {m}, Fib[x] = {Fib[x]}")
    x -= 1
    i = x
    if number[i] < find:  # i的初值也是确定的。
        i += m
    while Fib[x] > 0:  # 搜寻，x值不断减小，范围越来越小，搜寻越来越精细
        if number[i] < find:  # 小于被搜寻的值
            i += Fib[x - 1]  # 右移搜寻位置
            x -= 1
        elif number[i] > find:  # 大于被搜寻值
            i -= Fib[x - 1]  # 左移搜寻位置
            x -= 1
        else:
            return i  # 相等，找到
    return -1  # 搜寻步子已经最小，还是没找到，搜寻结束

c = fibsearch(number, find, Fib)
print("fibsearch 函数的返回值：", c)
# 结束时间
end = datetime.datetime.now()
# 输出
print("final is in ", end - start)
