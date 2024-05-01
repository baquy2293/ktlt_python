# bình phương có lặp
def binhphuonglap(a, k, n):
    k = nhiphan(k)
    b = 1 if k[0] == 0 else a
    for i in range(1, len(k)):
        a = (a * a) % n
        if k[i] == 1:
            b = (b * a) % n
    return b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# nhị phân
def nhiphan(number):
    binary = []
    while number > 0:
        a = number % 2
        binary.append(a)
        number = number // 2
    return binary


# milerrabin


# số nghịch đảo


print(binhphuonglap(41, 101, 211))
