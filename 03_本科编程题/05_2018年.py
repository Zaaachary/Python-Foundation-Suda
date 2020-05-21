"""
重写了一遍2018年的编程题
"""
def func1(m: int, n: int):
    """
    判断是否互质
    """
    if n <= 1 or m <= 1:
        return None

    if n > m:
        n, m = m, n

    for i in range(2, n+1):
        if m % i == 0 and n % i == 0:
            return False
    else:
        return True


def func2(L: list):
    """
    统计逆序数
    """
    if len(L) <= 1:
        return 0

    count = 0
    for index, num1 in enumerate(L):
        for num2 in L[index+1:]:
            if num2 < num1:
                count += 1
    return count


def func3(mat1, mat2):
    """
    矩阵乘法
    """
    m, n = len(mat1), len(mat2[0])
    mat3 = []
    for i in range(m):
        mat3.append([])
        for j in range(n):
            # mat1 的第i行 * mat2 的第j列
            temp = [v1 * v2 for v1,
                    v2 in zip(mat1[i], [mat2[k][j] for k in range(len(mat2))])]
            mat3[i].append(sum(temp))
    return mat3


def func4(onedim: list):
    """
    一维转二维  按个处理
    """
    # 
    ans = []
    n = int(len(onedim) ** (1/2))
    # i:0, n, 2n, 3n...   + j:0~n-1
    ans = [[onedim[i+j] for j in range(n)] for i in range(0, len(onedim), n)]
    return ans


def func4_2(onedim:list):
    """
    一维转二维  切片 按行处理
    """
    l = len(onedim)
    n = int(l**(1/2))
    ndim = []
    for i in range(n):
        ndim.append(onedim[i*n:i*n+n])
    return ndim


def func5(S: str):
    """
    统计词频，返回最高频三个单词
    """
    from collections import Counter
    word_list = S.split(' ')
    word_dict = Counter(word_list)
    word_list = sorted(word_dict, key=lambda x: word_dict[x], reverse=True)
    return word_list[:3]


def func6(S, T):
    """
    Jaccard系数J
    """
    S, T = set(S), set(T)
    a = len(S & T) # 两个单词都出现的个数
    b = len(S-T)
    c = len(T-S)
    # J =  a / (a+b+c)
    return (a,b,c)


def func7(string):
    """
    寻找字符串中出现频率最高的字符
    """
    ch_dict = {}
    for ch in string:
        ch = ch.upper()
        ch_dict[ch] = ch_dict.get(ch, 0) + 1
    max_freq, max_ch = 0, None
    for k, v in ch_dict.items():
        if v > max_freq:
            max_freq = v
            max_ch = k
    return [max_ch, max_freq]


def func8(string):
    """
    匹配正整数并按数字均值排序
    """
    def compute(num):
        count = 0
        while num > 0:
            num, m = divmod(num, 10)
            count += m
        return count
    
    import re
    pattern = r'[+\-]?\d+'
    # num_list = re.findall(pattern, string)    # 返回所有数字 正整数负整数  如-123456 不会只被识别成12345
    num_list = [num for num in map(int, re.findall(pattern, string)) if num > 0 and 100 <= num <= 99999]
    num_list.sort(key=compute, reverse=True)
    return num_list
    
    
if __name__ == "__main__":
    print(func1(3, 2))
    print(func2([1, 3, 2, 4]))
    print(func3([[1, 2], [1, 3]], [[1, 1], [1, 0]]))
    print(func4([2, 1, 3, 4]))
    print(func5('hello hi hello apple'))
    print(func6('his', 'she'))
    print(func7('AbaaaCC'))
    # print(func8('+123333a-4567 1234'))
    print(func8('123a4567 1'))