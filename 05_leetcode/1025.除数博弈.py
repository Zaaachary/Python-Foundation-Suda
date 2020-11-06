"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

- 选出任一 x，满足 0 < x < N 且 N % x == 0 。
- 用 N - x 替换黑板上的数字 N 。

如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以 最佳状态 参与游戏。
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        # 可以证明N为偶数时 爱丽丝必胜
        return N%2 == 0

if __name__ == "__main__":
    S = Solution()
    print(S.divisorGame(4))