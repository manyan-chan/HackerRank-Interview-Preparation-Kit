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
