import random

"""
O(n*log(n))

T(n) = aT(n/b) + f(n)
a, b >= 1
"""


def merge_sort(A):
    print("Splitting ", A)
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i = i + 1
            else:
                A[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", A)


def main():
    unsorted = [random.randint(0, 20) for i in range(20)]

    merge_sort(unsorted)

if __name__ == "__main__":
    main()
