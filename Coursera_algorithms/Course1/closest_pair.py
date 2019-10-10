# 1. sort coords(x, after y)
# sort is canonical primitive which we can user costless
import random
import math
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(1000)

def d(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute(ax):
    mi = d(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                dist = d(ax[i], ax[j])
                if dist < mi:  # Update min_dist and points
                    mi = dist
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi


def ClosestPair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)

    q = ax[:ln_ax]
    r = ax[ln_ax:]

    qx = sorted(q, key=lambda x: x[0])
    qy = sorted(q, key=lambda x: x[1])

    rx = sorted(r, key=lambda x: x[0])
    ry = sorted(r, key=lambda x: x[1])

    (p1, q1, dist1) = ClosestPair(qx, qy)
    (p2, q2, dist2) = ClosestPair(rx, ry)

    if dist1 < dist2:
        delta = dist1
        min_pair = (p1, q1)
    else:
        delta = dist2
        min_pair = (p2, q2)

    # delta = min(d(p1, q1), d(p2, q2))
    (p3, q3), dist3 = ClosestSplitPair(ax, ay, delta)

    if delta < dist3:
        return min_pair[0], min_pair[1], delta
    else:
        return p3, q3, dist3
        


def ClosestSplitPair(px, py, delta):
    x_max = max(px, key=lambda x: x[0]) // 2
    py = [x for x in py if (x[0] >= x_max - delta) and (x[0] <= xmax + delta)]
    best = delta
    best_pair = None

    for i in range(len(sy) - 1):
        for j in range(min(7, len(sy) - i)):
            p, q = py[i], py[i+j]
            if d(p, q) < best:
                best_pair = (p, q)
                best = d(p, q)
    return best_pair, best

if __name__ == "__main__":
    points = [(random.randint(0, 5), random.randint(5, 10)) for _ in range(6)]
    print(points)
    
    split = len(points) // 2
    L = points[:split]
    R = points[split:]

    p1, p2, delta = ClosestPair(L, R)
    print(p1, p2, delta)

    # plot
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    plt.scatter(xs, ys)
    plt.show()