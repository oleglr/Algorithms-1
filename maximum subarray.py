from Sorting.generate_array import generate_list
import sys

sys.setrecursionlimit(20000)

def find_max_cross_subarray(A, low, mid, high):

    # left part
    left_sum = -float('inf')
    sum_l = 0
    for i in range(mid, low-1, -1):
        sum_l = sum(A[i:mid])
        if sum_l > left_sum:
            left_sum = sum_l
            max_left = i

    # right part
    right_sum = -float('inf')
    sum_r = 0
    for j in range(mid+1, high+1):
        sum_r = sum(A[mid+1:j])
        if sum_r > right_sum:
            right_sum = sum_r
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def find_max(A, low, high):
    if high == low:
        return (low, high, A[int(low)])

    else:
        mid = int((low+high) / 2)
        # left part
        left_low, left_high, left_sum = find_max(A, low, mid)
        # right part
        right_low, right_hight, right_sum = find_max(A, mid+1, high)

        # cross part
        cross_low, cross_high, cross_sum = find_max_cross_subarray(
            A, low, mid, high
        )
        # vetvleniya
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_hight, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

if __name__ == "__main__":
    ls = generate_list(20)
    low, high, all_sum = find_max(ls, 0, 19)

    print(f'Original array: {ls}\n')
    print(f'left: {low}\tright: {high}\tsum: {all_sum}')