from collections import Counter

def func1(num):
    """
    给出一个整数n，请计算并返回该整数「各位数字之积」与「各位数字之和」的差。
    """
    add_sum, mul_sum = 0, 1
    while num != 0:
        num, m = divmod(num, 10)
        add_sum += m
        mul_sum *= m
    return mul_sum - add_sum


def func2(lst:[]):
    """
    给你一个整数列表lst，请你帮忙统计数组中每个数的出现次数。
    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
    """
    from collections import Counter
    num_freq = Counter(lst)
    freq_set = set(num_freq.values())
    # 有无重复的频数
    return True if len(freq_set) == len(num_freq.values()) else False


def func3(lst:[]):
    """
    给定一个非负整数列表lst，返回lst的排序结果，
    排序要求首先是奇数在前，偶数在后，然后是按照数字从大到小排序。
    """
    return sorted(lst, key=lambda num: (num%2, -num), reverse=True)


def func4(s:str, t:str):
    """
    给定两个字符串 s 和 t，它们只包含小写字母。
    字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。请找出在 t 中被添加的字母。
    """
    s_dict = Counter(s)
    t_dict = Counter(t)
    for ch in t_dict:
        # s中没有ch 或者 s中ch的次数比t少1
        if ch not in s_dict or t_dict[ch] - s_dict[ch]==1:
            return ch


def func5(str1):
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。
    """
    stack = []
    trans_dict = {')':'(', '}':'{', ']':'['}
    for ch in str1: # 遍历字符串
        if ch in "({[":
            stack.append(ch)
        elif len(stack) > 0:    # ch是)]}且栈内有元素
            temp = stack.pop()
            if temp != trans_dict[ch]:
                return False
        else:
            return False
    else:
        return True if len(stack) == 0 else False   # 栈空则都匹配上了



if __name__ == "__main__":
    print(func1(123))   # 0
    # print(func1(1234))  # 24-10
    print(func2([1,2,2,1,1,3])) # True
    # print(func2([1,2,2,1,4,3]))
    print(func3([1,2,3,4,5,6]))
    print(func4("abcd", "abcde"))
    print(func5("{}[]()"))
    # print(func5("{}[()]"))
    # print(func5("{[]()"))