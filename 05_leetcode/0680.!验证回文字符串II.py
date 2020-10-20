"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 200ms 26%
        front, rear = 0, len(s)-1
        if rear <= 1:
            # 长度小于等于2的字符串满足
            return True

        def notmatch(front, rear):
            while front < rear:
                # 找到发生不匹配的位置
                if s[front] == s[rear]:
                    front += 1
                    rear -= 1
                else:
                    return (front, rear)
            else:
                return False
        
        result = notmatch(front, rear)
        if not result:
            return True
        else:
            front, rear = result
            return (not notmatch(front+1, rear)) or (not notmatch(front, rear-1))

    def validPalindrome2(self, s):
        # 128ms 57.71 更好的写法
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s, left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    test = "abca"
    S = Solution()
    print(S.validPalindrome(test))