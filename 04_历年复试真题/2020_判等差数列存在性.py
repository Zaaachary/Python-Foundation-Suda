"""
2020年Python复试上机编程题（仅一道，20分钟完成）：
编写函数check(L) 验证整数列表L中是否存在5个数，可以构成一个公差为1的等差数列。

具体说明：
    1. 列表L中的元素一定是整数，函数中无需验证L中元素的类型
    2. 列表L的长度不小于5，函数中无需考虑L的长度不足5的情况
    3. 如果列表L中有符合要求的等差数列，函数返回True 否则返回False

编写程序测试check代码的正确性，提交的源代码可以包括测试代码，也可以不包括

评分说明
    1. 评分只考察 check函数的内容
    2. 函数有语法错误或运行发生异常均不得分
"""

def check(L):
    """
    思路：将L排序 判断是否存在连续5个数相差为1
    考试的时候完成的 缺少了去重
    """
    L.sort()    # 从小到大排序
    for index in range(0, len(L)-4):
        count = 0
        for i in range(4):
            # 判断index后的5个数是否依次满足关系
            if L[index+i+1] - L[index+i] == 1:
                count += 1
            else:
                count = 0
                break
        if count == 4:
            return True
    return False


def check2(L):
    """
    思路：将L排序 判断是否存在连续5个数相差为1
    考试后写的正解
    """
    S = set(L)
    L = sorted(S)    # 从小到大排序
    if len(L) < 5:
        return False
    for index in range(0, len(L)-4):
        count = 0
        for i in range(4):
            # 判断index后的5个数是否依次满足关系
            if L[index+i+1] - L[index+i] == 1:
                count += 1
            else:
                count = 0
                break
        if count == 4:
            return True
    return False


if __name__ == "__main__":
    print(check([1, 2, 3, 4, 5, 6]))
    print(check([1, 3, 5, 6, 7, 8, 10, 9]))
    print(check([1, 2, 3, 4, 6]))
    print(check([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    print(check([1, 1, 1, 1, 1, 2, 3, 4]))
