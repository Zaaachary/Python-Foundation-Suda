
# 输入n  找出1~n 中 二进制1比0多的数

def find_number(n):
    a=[]
    for i in range(1,n+1):
        s=bin(i)[2:]
        if s.count('1')>s.count('0'):
            a.append(i)
    return a

if __name__ == "__main__":
    pass