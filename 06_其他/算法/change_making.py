#! -*- encoding:utf-8 -*-
"""
@File    :   change_making.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   找零问题
"""

def change(money, deno):
    # deno: 面额列表; money: 要找零的总金额
    deno.sort(reverse=True)
    result = []
    current = 0

    while money != current:
        for x in deno:
            if current + x <= money:
                result.append(x)
                current += x
                break
        else:
            return None     # no solution found
    return result


if __name__ == "__main__":
    denomination = [100,25,10,5,1]
    money = 378

    print(change(money, denomination))
    

