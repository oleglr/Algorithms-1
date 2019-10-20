import random
import math
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

def partition(arr, low, high): 
    i = low - 1
    pivot = arr[high]
  
    for j in range(low , high): 
        if arr[j] <= pivot:
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i+1 
  
def quickSort(arr, low, high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

ls = [random.randint(0, 10) for _ in range(6)]
print('Source array ', ls)
quickSort(ls, 0, len(ls)-1)
print('Sorted array ', ls)


########################################
# SECOND VARIANT

def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)
	
def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)
	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]