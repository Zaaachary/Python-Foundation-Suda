#! -*- encoding:utf-8 -*-
"""
@File    :   Similarity.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
"""

class Comparator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def max_substr(self):
        '''
        compute the max_substr_len of the two str
        '''
        max_len = 0
        if '' in [self.str1, self.str2]:
            return max_len

        if len(self.str1) > len(self.str2):     # let len(str1) < len(str2)
            self.str1, self.str2 = self.str2, self.str1
        # compute max_substr len
        for length in range(1, len(self.str1)+1):
            for i in range(0, len(self.str1)-length+1):
                # print(self.str1[i:i+length])
                if self.str1[i:i+length] in self.str2:    # if exist sub_str of length
                    max_len = max(max_len, length)
                    break
        return max_len
        # return max_len / len(self.str1)
        # return max_len / len(self.str2)  # switch to long word

    def max_substr_score(self, min_word=False):
        '''
        evaluate similarity by len(max_substr)/len(max_str) 
        '''
        if min_word:
            return self.max_substr() / len(self.str1) if len(self.str1) !=0 else 'inf'
        else:
            return self.max_substr() / len(self.str2)

    def edit_distance(self):
        '''
        compute edit_distance with dynamic programming speedup.  O(m*n)
        '''
        if '' in [self.str1, self.str2]:
            return max(len(self.str1), len(self.str2))

        # dpmatrix [len(str1)+1] x [len(str2)+1]
        dpmatrix = [[-1 for i in range(len(self.str2)+1)] for j in range(len(self.str1)+1)]
        for i in range(0, len(self.str1)):
            dpmatrix[i][0] = i
        for j in range(0, len(self.str2)):
            dpmatrix[0][j] = j

        for i in range(1, len(self.str1)+1):
            for j in range(1, len(self.str2)+1):
                if self.str1[i-1] == self.str2[j-1]:
                    dpmatrix[i][j] = dpmatrix[i-1][j-1]
                else:
                    dpmatrix[i][j] = dpmatrix[i-1][j-1] + 1
                
                dpmatrix[i][j] = min(dpmatrix[i][j], dpmatrix[i-1][j]+1, dpmatrix[i][j-1]+1)
        
        return dpmatrix[len(self.str1)][len(self.str2)]
    
    def edit_distance_score(self, min_word=False):
        '''
        evaluate similarity by edit_distance/len(max_str)
        '''
        if min_word:
            m = min(len(self.str1), len(self.str2))
        else:
            m = max(len(self.str1), len(self.str2))
        return self.edit_distance() / m if m != 0 else 1

    def cph_score(self, min_word=False):
        '''
        Comprehensive score
        '''
        return self.edit_distance_score(min_word) - self.max_substr_score(min_word)

    # def edit_distance_recur(self, i=0, j=0):
    #     '''
    #     evaluate similarity by edit_distance
    #     recursion method, it's OK for words comparison.
    #     '''
    #     if i>=len(self.str1) or j>=len(self.str2):
    #         return max(len(self.str1)-i, len(self.str2)-i)
    #     elif self.str1[i] == self.str2[j]:
    #         return self.edit_distance_recur(i+1, j+1)
    #     else:
    #         L1 = self.edit_distance_recur(i+1, j+1) + 1     # replace one of str1[i] and str2[j]
    #         L2 = self.edit_distance_recur(i, j+1) + 1       # del str2[j] or add char to str1[i]
    #         L3 = self.edit_distance_recur(i+1, j) + 1       # del str1[i] or add char to str2[j]
    #         return min(L1, L2, L3)


if __name__ == "__main__":
    origin = 'sorrowful'
    synonym_list = ['sad', 'unhappy']


    for synonym in synonym_list:
        print('\nsimilarity between "{}" and "{}"'.format(origin, synonym))
        c = Comparator(origin, synonym)
        print('max_substr:{}, score:{}'.format(c.max_substr(), c.max_substr_score(True)))
        print('edit_dist:{}, score:{}'.format(c.edit_distance(), c.edit_distance_score(True)))
        print('comprehensive_score:', c.cph_score(True))


"""
Reference
1. https://www.jianshu.com/p/ebc4b26d8136
2. https://blog.csdn.net/qq_19917979/article/details/89366185
3. https://blog.csdn.net/qq_41582941/article/details/83719839
"""