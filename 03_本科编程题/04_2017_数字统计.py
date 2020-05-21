import random
from collections import Counter


def productRndNum():
    rnd = random.randint(100, 200)
    numberLst = [random.randint(100, 500) for _ in range(rnd)]
    return numberLst


def getDigNumber(numberLst, digLst):
    # 返回numberLst中存在digLST数字
    ans = []
    for num in numberLst:
        n = num
        while n != 0:
            n, m = divmod(n, 10)
            if m in digLst:
                ans.append(num)
                break
    return ans


def printOut(numLst, row):
    current = 0
    print("num26Lst:")
    for num in numLst:
        print('{: >5}'.format(num), end='')
        current += 1
        if current == row:
            current = 0
            print('')
    if num % row != 0:
        print('')


def getDivisorNum(numLst):
    ans = []
    for num in numLst:
        for i in range(2, int(num**(1/2))+1):
            if num%i != 0:
                ans.append(i)
    return ans


def staticResult(numLst):
    num_dict = Counter(numLst)
    return num_dict
    

def printMax5Out(num_dict):
    top5 = sorted(num_dict, key=lambda x:num_dict[x], reverse=True)[:5]
    print("出现次数最多的5个因子：")
    for num in top5:
        print(num)


def delMultiDivisor(numLst):
    # 要在原地删除 不改变id
    temp = list(set(numLst))
    numLst.clear()
    numLst.extend(temp)


def printDivisorToFile(filename, numLst):
    # 输出到文件
    f = open(filename, 'w')
    current = 0
    for num in numLst:
        f.write('{: >5}'.format(num))
        current += 1
        if current == 9:
            current = 0
            f.write('\n')
    f.close()

    # 输出到命令行
    current = 0
    for num in numLst:
        print('{: >5}'.format(num), end='')
        current += 1
        if current == 8:
            current = 0
            print('')
    if num % 8 != 0:
        print('')


if __name__ == "__main__":
    # ----产生随机整数-------
    numberLst = productRndNum()

    # ----找出包含数字 2 或 6 的整数，其中 digLst 包含数字 2 和 6-----
    digLst = [2, 6]
    num26Lst = getDigNumber(numberLst, digLst)
    printOut(num26Lst, 8)

    #-----找出所有整数的因子-----
    resultLst = getDivisorNum(num26Lst)

    #-----统计每个因子出现的次数-----
    resultStatic = staticResult(resultLst)
    printMax5Out(resultStatic)

    # ----删除 resultLst 中重复因子的多余份数，只保留一份-----
    delMultiDivisor(resultLst)
    print("===出现次数最多的数字===")
    printDivisorToFile(".\\Files\\04_result.txt", resultLst)
