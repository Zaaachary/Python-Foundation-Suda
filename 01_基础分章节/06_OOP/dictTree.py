"""
字典树
受保护的
"""

class Node(object):   # object  之后Node可以被继承
    '''
    字典树普通节点
    '''
    def __init__(self, value):
        self._children = {}  # 存储映射关系 字符边
        self._value = value   # None 表示映射 有value表示对应一个词
    
    def _add_child(self, char, value, overwrite=False):
        child = self._children.get(char, None)
        if child is None:
            child = Node(value)
            self._children[char] = child
        elif overwrite:
            child._value = value
        return child


class Trie(Node):
    '''
    字典树根节点
    '''
    def __init__(self):
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        state = self
        for char in key:
            state  = state._children.get(char)
            if state is None:
                return None # 未找到
        else:
            return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            if i < len(key) - 1: # 没有到最后一个结点
                state = state._add_child(char, None, False)
            else:
                state = state._add_child(char, value, True)

if __name__ == "__main__":
    trie = Trie()
    # 增 __setitem__()
    trie['人工'] = 'artificial'
    trie['人工智能'] = 'AI'
    trie['入门'] = 'introduction'
    assert '人工' in trie  # __contains__

    # 删
    trie['人工'] = None
    assert '人工' not in trie

    # 改
    trie['人工智能'] = 'artificial intelligence'
    print(trie['人工智能'])

    # 查
    print(trie['入门'])