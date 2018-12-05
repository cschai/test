#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 14:32
# @Author  : hbw
# @File    : 快速排序.py
# @Software: PyCharm
import random
def sort_q(array,l,r):    #array队列、列表
    if l<=r:
        # 拿基准元素的下标
        position=p(array,l,r)
        # 排序左边列表
        sort_q(array,l,position-1)
        # 排序右边列表
        sort_q(array,position+1,r)

def p(array,l,r):
    x=array[r]
    index=l  # 拿基准元素前面的元素做为交换
    for i in range(l,r): # 取数组的下标  便于更换数组的元素
        # 当数组元素大于基准元素的时候
        if array[i]<=x:
            # 将数组更换到数组的后端，同时记录更换的次数
            array[index],array[i]=array[i],array[index]
            index += 1
    #将最后一个大于基准元素的元素和基准元素做交换
    array[index],array[r]=array[r],array[index]
    return index
    # x=array[r]
    # index=r  # 拿基准元素前面的元素做为交换
    # for i in range(l,r): # 取数组的下标  便于更换数组的元素
    #     # 当数组元素大于基准元素的时候
    #     if array[i]>x:
    #         # 将数组更换到数组的后端，同时记录更换的次数
    #         array[index],array[i]=array[i],array[index]
    #         index -= 1
    # #将最后一个大于基准元素的元素和基准元素做交换
    # array[index],array[r]=array[r],array[index]
    # return index
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

if __name__ == '__main__':
    l=list(range(10))
    random.shuffle(l)
    print(l)
    # l=quick_sort(l)
    # print(l)
    sort_q(l,0,len(l)-1)
    print(l)