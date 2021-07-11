
# [{1,2},{1,2,3}]
# 数组包含很多集合，集合都是一些数字， 然后返回数字  出现频率大于 [数组长度/2](下标)
def find_major(L):
    s = len(L)//2
    m = {}
    result = set()
    for i in L:
        for j in i:
            m[j] = m.get(j, 0)+1
    for key, value in m.items():
        if value > s:
            result.add(key)
    if len(result) == 0:
        return None
    return result


if __name__ == "__main__":
    pass
