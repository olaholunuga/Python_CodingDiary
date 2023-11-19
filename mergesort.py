#!/usr/bin/env python

def merge(firstArr, secondArr):
    new_arr = []
    len_f = len(firstArr)
    len_s = len(secondArr)
    i = 0
    j = 0
    while(i < len_f and j < len_s):
        if firstArr[i] < secondArr[j]:
            new_arr.append(firstArr[i])
            i += 1
        else:
            new_arr.append(secondArr[j])
            j += 1
    if i < len_f:
        for x in range(i, len_f):
            new_arr.append(firstArr[x])
    if j < len_s:
        for x in range(j, len_s):
            new_arr.append(secondArr[x])
    print(new_arr)
    return new_arr

def mergesort(arr):
    len_arr = len(arr)
    mid = len_arr // 2
    if len_arr <= 1:
        return arr
    s1 = mergesort(arr[:mid])
    s2 = mergesort(arr[mid:])
    return merge(s1, s2)
        
l1 = [2, 3, 5]
l2 = [1, 4, 7]
print(merge(l1, l2))
print(mergesort([4, 2, 3, 9, 0, 8, 5, 7, 1, 6]))