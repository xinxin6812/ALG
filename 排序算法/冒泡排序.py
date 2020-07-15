def bubble_sort(array):
    for i in range(len(array) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(array) - i - 1):  # j为列表下标
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

