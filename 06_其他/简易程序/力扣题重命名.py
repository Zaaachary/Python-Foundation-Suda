"""
Leetcode 文件夹中的文件序号 在小于4位数的序号前面补零

"""
import os
import re

class FileRenamer:
    def __init__(self, targetdir='./'):
        self.targetdir = targetdir
        os.chdir(targetdir)
        print('Now working at ' + os.getcwd())

    def changedir(self, targetdir):
        print("Changing working directory")
        self.__init__(targetdir)

    def renamenumber(self, length):
        """
        length: 目标数字序号长度
        """
        pattern = re.compile(r'^\d+')
        # pattern = re.compile(r'^\d+_')
        for filename in os.listdir():
            # if number := pattern.match(filename):   # 海象运算符
            number = pattern.match(filename)
            if number:
                number = number.group()
            else:
                continue

            characters = filename[len(number):]
            num = int(number)
            # num = int(number[:-1])
            number = str(num).rjust(length, '0')
            # number = str(num).rjust(length, '0')+'.'
            dst = number + characters
            print(dst)
            os.rename(src=filename, dst=dst)
        print("改名完成")

if __name__ == "__main__":
    F = FileRenamer()
    # F.changedir('./06_其他')
    F.changedir('./05_leetcode')
    F.renamenumber(4)