

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
    奇奇怪怪的规律
    """
    m = len(A)
    B = [[] for _ in range(2 * m-1)]

    def nextelemt():
        for i in range(2*m-1):
            j = 0
            while 0 <= i < m or 0 <= j < m:                
                if 0 <= i < m and 0 <= j < m:
                    yield A[i][j]
                i -= 1
                j += 1
                
    nextnum = nextelemt()
    current = 1
    for i in range(2*m-1):
        for j in range(current):
            B[i].append(next(nextnum))
        B[i].extend([0]*(m-current))
        if i < m-1:
            current += 1
        else:
            current -= 1
    return B


def func4_2(A):
    # 实现方法2
    m = len(A)
    B = [[0]*m for _ in range(2*m-1)]
    for i in range(m):
        for j in range(m):
            if i + j < m:
                B[i+j][j] = A[i][j]
            else:
                B[i+j][m-i-1] = A[i][j]
    return B


def func5(w: str):
    if len(w) <= 1:
        return w.upper()
    Capital = False
    ans = ''
    for ch in w:
        if ch.isupper():
            Capital = True
            break
    ans += w[0].upper()
    ans += w[1:-1].lower()
    if Capital:
        ans += w[-1].lower()
    else:
        ans += w[-1].upper()
    return ans
    

def func6(s:str):
    """
    英文数字 正文； 其他字符 分隔符
    用一个空格替换分隔符
    单词长度仅5个字符 大于部分除首尾字符换成*
    """
    import re
    word_list = re.findall(r'\w+', s)
    for index, word in enumerate(word_list):
        if len(word) >5:
            word_list[index] = word[0] + '*'*(len(word)-2) +word[-1]
    return ' '.join(word_list)


def func7(words:list, chars:str):
    """
    words n个单词
    chars 字符串 m字母 大小写
    chars 中字母拼words中的单词
    chars 中每个字母用一次
    放回掌握的单词数
    """
    from collections import Counter
    ch_orgdict = Counter(chars)
    count = 0
    for word in words:
        ch_tempdict = ch_orgdict.copy()
        for ch in word:
            if ch_tempdict.get(ch, 0):
                ch_tempdict[ch] -= 1
            else:
                break
        else:
            count += 1
    return count


def func8(lst):
    """
    lst 若干元组的列表  元组含字符串和整数
    字符串存了学号 9位  整数存了时间 1~3合法
    除去时间或学号不合法的记录
    计算每位同学总时间，降序排列，时间相同学号升序
    元组形式返回排名第一的同学
    """
    stu_dict = {}
    for record in lst:
        number, time = record
        if len(number) == 9 and number.isdigit() and 1<=time<=3:
            stu_dict[number] = stu_dict.get(number, 0) + time
    # 两次sort
    # stu_list = sorted(stu_dict)
    # stu_list.sort(key=lambda x:stu_dict[x], reverse=True)
    # 一次sort
    stu_list = sorted(stu_dict, key=lambda x: (-stu_dict[x], x))

    if stu_list:
        return (stu_list[0], stu_dict[stu_list[0]])
    else:
        return None

if __name__ == "__main__":
    print('1:', func1(-1,2))
    print('2:', func2(0, 0, 11))
    print('3:', func3([1, 234, 5, 6, 7, 890]))
    print('4:', func4_2([[1,2,3],[4,5,6],[7,8,9]]))
    print('5:', func5("w"))
    print('6:', func6("hello!world, computer,,,class,52,5w"))
    print('7:', func7(["cat", 'bt', 'hat', 'tree'], "atach"))
    print('8:', func8([("192740506",3), ("192740101",2), ("192740101",2)]))
