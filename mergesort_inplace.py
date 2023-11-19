#!/usr/bin/env python

def merge(data, start, mid, end):
    temp = []
    i = start
    j = mid + 1
    if end - start == 1:
        if data[start] > data[end]:
            data[start], data[end] = data[end], data[start]
        return
    while i < mid and j < end:
        if data[i] < data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1
    if i < mid:
        for x in range(i, mid + 1):
            temp.append(data[x])
    if j < end:
        for x in range(j, end + 1):
            temp.append(data[x])
    print(temp)
    for k, a in enumerate(temp, start):
        data[k] = a
    

def mergesort(data, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(data, start, mid)
        mergesort(data, mid + 1, end)
        merge(data, start, mid, end)

data2 = [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
data = [4, 2, 3, 9, 0, 8, 5, 7, 1, 6]
#merge(data2, 0, 2, 10)
mergesort(data, 0, len(data) - 1)