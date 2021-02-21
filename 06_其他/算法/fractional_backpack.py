#! -*- encoding:utf-8 -*-
"""
@File    :   fractional_backpack.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://blog.csdn.net/cPen_web/article/details/111873620
"""

def fractional_backpack(goods, w):   # 参数 商品、w背包重量
    # 贪心拿商品，拿单位重量更值钱的商品，所以先对goods进行排序
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)  # 按照单位价格降序排列
    m = [0 for _ in range(len(goods))]                   # m表示每个商品拿多少，存结果的
    total_v =0                                           # 存结果的 拿走的总价值
    for i, (price,weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1                                      # 这个商品拿多少。拿1整个，或者小数
            total_v += price                              # 更新拿走的 价值
            w -= weight                                   # 并更新w的值 (背包重量)
        else:
            m[i] = w / weight
            total_v += m[i] * price                       # 更新拿走的 价值
            w = 0                                         # 背包满了
            break
    return total_v, m                                     # 最后返回 存结果的m、total_v

if __name__ == "__main__":
    goods = [(60, 10), (100, 20), (120, 30)]    # 每个商品元组表示  (价格，重量)
    print(fractional_backpack(goods, 50))
    #结果为
    # (240.0, [1, 1, 0.6666666666666666])
