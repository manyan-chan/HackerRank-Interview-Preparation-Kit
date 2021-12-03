# Warm-up challenges
def sockMerchant(n, ar):
    pairs = 0
    socks = set()
    for sock in ar:
        if sock in socks:
            pairs += 1
            socks.remove(sock)
        else:
            socks.add(sock)
    return pairs


def countingValleys(steps, path):
    valleys = 0
    level = 0
    for step in path:
        if step == "U":
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
            jumps += 1
        else:
            i += 1
            jumps += 1
    return jumps


def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")


# Arrays
def hourglassSum(arr):
    sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            sums.append(
                sum(arr[i][j : j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j : j + 3])
            )
    return max(sums)


def rotLeft(a, d):
    return a[d:] + a[:d]


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swaps += 1
    return swaps


def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        arr[query[0] - 1] += query[2]
        if query[1] <= n:
            arr[query[1]] -= query[2]
    max_val = 0
    val = 0
    for i in range(len(arr)):
        val += arr[i]
        if val > max_val:
            max_val = val
    return max_val
