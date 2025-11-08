import math
import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# Distance function
# -----------------------------
def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

# -----------------------------
# Brute-force closest pair
# -----------------------------
def brute_force_closest_pair(points):
    best_distance = float('inf')
    best_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < best_distance:
                best_distance = d
                best_pair = (points[i], points[j])
    return best_distance, best_pair

# -----------------------------
# Divide-and-conquer closest pair
# -----------------------------
def closest_pair_dc(points):
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])
    return _closest_pair_rec(Px, Py)

def _closest_pair_rec(Px, Py):
    n = len(Px)
    if n <= 8:
        return brute_force_closest_pair(Px)
    
    mid = n // 2
    Qx = Px[:mid]; Rx = Px[mid:]
    midx = Px[mid][0]

    Qy = [p for p in Py if p[0] <= midx]
    Ry = [p for p in Py if p[0] > midx]

    d_left, pair_left = _closest_pair_rec(Qx, Qy)
    d_right, pair_right = _closest_pair_rec(Rx, Ry)

    if d_left < d_right:
        d = d_left
        best_pair = pair_left
    else:
        d = d_right
        best_pair = pair_right

    strip = [p for p in Py if abs(p[0] - midx) < d]

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= d:
                break
            dij = dist(strip[i], strip[j])
            if dij < d:
                d = dij
                best_pair = (strip[i], strip[j])

    return d, best_pair

# -----------------------------
# Experimental verification
# -----------------------------
def run_experiment():
    sizes = [100, 200, 400, 800, 1600, 3200, 6400]  # number of points
    times = []

    for n in sizes:
        points = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        start = time.time()
        closest_pair_dc(points)
        end = time.time()
        times.append(end - start)
        print(f"n={n}, time={end-start:.5f} s")

    # Plot runtime
    plt.figure(figsize=(8,5))
    plt.plot(sizes, times, marker='o', label='Measured time')
    plt.plot(sizes, [t*math.log2(n)/math.log2(100) for t,n in zip(times,sizes)], linestyle='--', label='O(n log n) reference')
    plt.xlabel("Number of points (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Closest Pair Algorithm Runtime")
    plt.legend()
    plt.grid(True)

    plt.savefig("closest_pair_runtime.png", dpi=300)
    print("Graph saved as 'closest_pair_runtime.png' in the current folder.")

    plt.show()

if __name__ == "__main__":
    run_experiment()
