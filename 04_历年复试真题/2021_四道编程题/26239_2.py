
# 查找一个数列中两个数相乘最大，如果两个pair 都是最大的就是相加起来最大的那个
def find_pair(L):
    if len(L) < 2:
        return[]
    x = L[0]
    y = L[1]
    m = L[0]*L[1]
    for index, i in enumerate(L):
        for j in L[index+1:]:
            c = i*j
            if c > m:
                x = i
                y = j
                m = c
            if c == m:
                if i+j > x+y:
                    x, y = i, j
    if x > y:
        x, y = y, x
    return (x, y)
