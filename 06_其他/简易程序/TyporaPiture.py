"""
通常 typora 的图片都存储于和 .md 文件相同的目录下的图片目录里
当然也不排除 .md 文件中有的图片不在上述文件夹中
此外 在文件编辑的过程中存在粘贴了某张图片 最后却不用该图片的情况
这种情况 就会是的上述文件夹里出现无用的图片

此程序正是用来应对 typora 的图片存储问题 程序主要实现了以下功能
1. 将目标目录中的 .md 中存于 其他目录的图片 复制到 目标目录下的图片目录
2. 清理目标目录下的图片目录 删除 .md 文件未使用的图片
"""
import os
import sys
import re
import argparse

class Cleaner:

    def __init__(self, targetdir='./'):
        self.targetdir = targetdir
        os.chdir(targetdir)
        print('Now working at ' + os.getcwd())

    def changedir(self, targetdir):
        print("Changing working directory")
        self.__init__(targetdir)

    def walk_through(self):
        pass


if __name__ == "__main__":
    pass