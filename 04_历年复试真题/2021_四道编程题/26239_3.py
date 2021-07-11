
#查找某一个数后面离它最近的比他大的数，如果没有就是none
#[1,3,5]   [3,5,none]
#[7,3,5]    [none,5,none]
def find_next(L):
    a=[None]*len(L)
    for index,i in enumerate(L):
        for j in L[index+1:]:
            if j>i:
                a[index]=j
                break
    return a

