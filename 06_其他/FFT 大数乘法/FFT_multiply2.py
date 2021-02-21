#! -*- encoding:utf-8 -*-
"""
@File    :   FFT_multiply2.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
import numpy as np
from decimal import Decimal


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x1_vec = list(map(int, list(reversed(num1))))
        x2_vec = list(map(int, list(reversed(num2))))

        extra_len = 1
        while 2**extra_len < len(x1_vec) + len(x2_vec):
            extra_len += 1
        N = 2**extra_len
        result = self.FFT_multiply(N=N, x1_vec=x1_vec, x2_vec=x2_vec)
        return str(result)

    def normal_multiply(self, N, x1_vec, x2_vec):
    # 不使用矩阵乘法版本：离散傅里叶变换
        W, A, B, C, D = [0] * N ** 2, [0] * N, [0] * N, [0] * N, [0] * N
        for k in range(N ** 2):
            W[k] = np.e ** complex(0, -(2 * np.pi) / N * k)  # 求W[k]的各次幂
        for k in range(len(A)):
            Xk = 0.0
            for n in range(len(x1_vec)):
                Xk += x1_vec[n] * W[k * n]
            A[k] = Xk
        for k in range(len(B)):
            Xk = 0.0
            for n in range(len(x2_vec)):
                Xk += x2_vec[n] * W[k * n]
            B[k] = Xk
        for i in range(len(C)):
            C[i] = A[i] * B[i]
        for n in range(len(D)):
            Xn = 0.0
            for k in range(len(C)):
                Xn += C[k] * 1 / W[k * n]
            D[n] = 1 / N * Xn
        return self.calc_all_number(np.array(D))

    def FFT_multiply(self, N, x1_vec, x2_vec):
        A = self.FFT(xn=np.array(x1_vec + [0] * (N - len(x1_vec))))
        B = self.FFT(xn=np.array(x2_vec + [0] * (N - len(x2_vec))))
        C = A * B
        D = self.IFFT(xk=C)
        return self.calc_all_number(D)

    def calc_all_number(self, D):
        result = 0
        for i in range(D.shape[0]):
            result += round(Decimal(D[i].real)) * 10 ** i
        return result

    def FFT(self, xn):
        N = xn.shape[0]
        N_min = min(N, 32)
        AX = self.DFT_slow(xn=xn.reshape((N_min, -1)))
        while AX.shape[0] < N:
            AX_even = AX[:, :int(AX.shape[1] / 2)]  # 偶数项多项式
            AX_odd = AX[:, int(AX.shape[1] / 2):]  # 奇数项多项式
            factor = np.exp(-2j * np.pi * np.arange(AX.shape[0]) / AX.shape[0] / 2)
            factor = factor.reshape((factor.shape[0], 1))
            factor_AX_odd = factor * AX_odd
            AX = np.vstack([AX_even + factor_AX_odd, AX_even - factor_AX_odd])
        return AX.ravel()

    def IFFT(self, xk):
        N = xk.shape[0]
        N_min = min(N, 32)
        AX = N_min * self.IDFT_slow(xk=xk.reshape((N_min, -1)))
        while AX.shape[0] < N:
            AX_even = AX[:, :int(AX.shape[1] / 2)]
            AX_odd = AX[:, int(AX.shape[1] / 2):]
            factor = np.exp(2j * np.pi * np.arange(AX.shape[0]) / AX.shape[0] / 2)
            factor = factor.reshape((factor.shape[0], 1))
            factor_AX_odd = factor * AX_odd
            AX = np.vstack([AX_even + factor_AX_odd, AX_even - factor_AX_odd])
        return 1 / N * AX.ravel()

    def DFT_slow(self, xn):
        # 计算离散傅里叶正变换：xk = ∑ xn * e**-(j*2pi*k*j/N)
        N = xn.shape[0]
        j = np.arange(N)
        k = j.reshape((N, 1))
        factor = np.exp(-2j * np.pi * k * j / N)
        return np.dot(factor, xn)

    def IDFT_slow(self, xk):
        # 计算离散傅里叶逆变换：xn = 1 / N * ∑ xk * e**(j*2pi*k*j/N)
        N = xk.shape[0]
        j = np.arange(N)
        k = j.reshape((N, 1))
        factor = np.exp(2j * np.pi * k * j / N)
        return 1 / N * np.dot(factor, xk)



if __name__ == "__main__":
    S = Solution()
    x1 = "12345670987281123213333123123213333333333333333331231231232123112132322101231233213333332131232131232132312312123213123123213214324323143243243231993146457656387648001273762153678236712763425461234567098728112321333312312321333333333333333333123123123212311213232210123123321333333213123213123213231231212321312312321321432432314324324323199314645765638764800127376215367823671276342546"
    x2 = "99987654321066661267812333333333333333333333124324234234231231231212321314324243144354765786985654694385903412903498234712349882131323214837598743819023901281231231212395679498624356123123784287564102134285466673987654321066661267812333333333333333333333124324234234231231231212321314324243144354765786985654694385903412903498234712349882131323214837598743819023901281231231212395679498624356123123784287564102134285466673"
    print(S.multiply(x1, x2))