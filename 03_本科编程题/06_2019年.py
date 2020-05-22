

def func1(x, y):
    """
    判定点的区域 正方形内1 上0 外-1
    """
    x_f, y_f = 0, 0
    if -1< x <1:
        x_f = 1
    elif x<-1 or x>1:
        x_f = -1

    if -1< y <1:
        y_f = 1
    elif y<-1 or y>1:
        y_f = -1
    
    if -1 in (x_f, y_f):
        return -1 # x，y至少有一个不在范围内
    elif 0 in (x_f, y_f):
        return 0
    else:
        return 1


def func2(d, L, R):
    """
    统计[L,R]中所有整数 中数字d出现次数
    """
    if not 0<=d<=9 or L>=R:
        return None
    count = 0
    for num in range(L, R+1):
        if num == 0 and d == 0:
            count += 1
        while num !=0:
            num, m = divmod(num, 10)
            if m == d:
                count += 1
    return count


def func3(num_list):
    """
    正整数列表 每个元素头尾部互换
    变换后质数切割序列 每个序列求和
    """
    # 字符串互换法
    ans = []
    for index, num in enumerate(num_list):
        num_str = str(num)
        ans.extend([int(num_str[0]), int(num_str[-1])])

    def isPrime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        else:
            return True

    temp = []
    for index in range(len(ans)-1, -1, -1):
        if isPrime(ans[index]):
            if len(temp)>0:
                # 遇到质数且temp中存有非质数
                num = int(''.join(map(str,temp[::-1])))
                ans.insert(index+1, num)
                temp.clear()
        else:
            temp.append(ans[index])
            ans.pop(index)
    else:
        if len(temp) > 0:
            num = int(''.join(map(str,temp[::-1])))
            ans.insert(0, num)
    return ans


def func4(A):
    """
    写错了 还没写完龟龟
    """
    m = len(A)
    B = [[] for _ in range(2 * m-1)]

    def nextelemt():
        # 产生L形序列 1 4 7 8 9  2 5 6  3
        col, flag = 0, True
        i, j = 0, 0
        while True:
            yield(A[i][j])
            i += 1
            if i == m -col: # 竖着
                i -= 1
                j += 1
                if j >= m:
                    col += 1
                    j = 0


    row = 2 * m -1 # 当前列非零的个数
    num = nextelemt()
    for column in range(m):
        for index in range(row):
            B[index].append(next(num))
        row -= 2

    return B

if __name__ == "__main__":
    print(func1(-1,2))
    print(func2(0, 0, 11))
    print(func3([1, 234, 5, 6, 7, 890]))
    print(func4([[1,2,3],[4,5,6],[7,8,9]]))