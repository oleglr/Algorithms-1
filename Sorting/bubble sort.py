from generate_array import generate_list

"""
O(n^2)
"""

def bubble_sort(arr):
    n = len(arr) - 1
    for _ in range(n):
        for j in range(n):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == "__main__":
    ls = generate_list(20)
    print(f"Old array: {ls}")

    new_array = bubble_sort(ls)
    print(f"New array: {new_array}")