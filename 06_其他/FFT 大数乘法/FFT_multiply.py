#! -*- encoding:utf-8 -*-
"""
@File    :   FFT_multiply.py
@Author  :   https://github.com/privateEye-zzy/Fourier_Transform
@Dscpt   :   大数乘法—多项式与快速傅里叶变换
"""
import numpy as np
from timeit import timeit
from decimal import Decimal

def calc_all_number(D):
    result = 0
    for i in range(D.shape[0]):
        result += round(Decimal(D[i].real)) * 10 ** i
    return result

# 计算离散傅里叶正变换：xk = ∑ xn * e**-(j*2pi*k*j/N)
def DFT_slow(xn):
    N = xn.shape[0]
    j = np.arange(N)
    k = j.reshape((N, 1))
    factor = np.exp(-2j * np.pi * k * j / N)
    return np.dot(factor, xn)

# 计算离散傅里叶逆变换：xn = 1 / N * ∑ xk * e**(j*2pi*k*j/N)
def IDFT_slow(xk):
    N = xk.shape[0]
    j = np.arange(N)
    k = j.reshape((N, 1))
    factor = np.exp(2j * np.pi * k * j / N)
    return 1 / N * np.dot(factor, xk)

def FFT(xn):
    N = xn.shape[0]
    N_min = min(N, 32)
    AX = DFT_slow(xn=xn.reshape((N_min, -1)))
    while AX.shape[0] < N:
        AX_even = AX[:, :int(AX.shape[1] / 2)]  # 偶数项多项式
        AX_odd = AX[:, int(AX.shape[1] / 2):]  # 奇数项多项式
        factor = np.exp(-2j * np.pi * np.arange(AX.shape[0]) / AX.shape[0] / 2)
        factor = factor.reshape((factor.shape[0], 1))
        factor_AX_odd = factor * AX_odd
        AX = np.vstack([AX_even + factor_AX_odd, AX_even - factor_AX_odd])
    return AX.ravel()

def IFFT(xk):
    N = xk.shape[0]
    N_min = min(N, 32)
    AX = N_min * IDFT_slow(xk=xk.reshape((N_min, -1)))
    while AX.shape[0] < N:
        AX_even = AX[:, :int(AX.shape[1] / 2)]
        AX_odd = AX[:, int(AX.shape[1] / 2):]
        factor = np.exp(2j * np.pi * np.arange(AX.shape[0]) / AX.shape[0] / 2)
        factor = factor.reshape((factor.shape[0], 1))
        factor_AX_odd = factor * AX_odd
        AX = np.vstack([AX_even + factor_AX_odd, AX_even - factor_AX_odd])
    return 1 / N * AX.ravel()

# 不使用矩阵乘法版本：离散傅里叶变换
def normal_multiply(N, x1_vec, x2_vec):
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
    return calc_all_number(np.array(D))

# 使用矩阵乘法版本：离散傅里叶变换
def DFT_multiply(N, x1_vec, x2_vec):
    A = DFT_slow(xn=np.array(x1_vec + [0] * (N - len(x1_vec))))
    B = DFT_slow(xn=np.array(x2_vec + [0] * (N - len(x2_vec))))
    C = A * B
    D = IDFT_slow(xk=C)
    return calc_all_number(D)

# 使用矩阵乘法版本：快速傅里叶变换
def FFT_multiply(N, x1_vec, x2_vec):
    A = FFT(xn=np.array(x1_vec + [0] * (N - len(x1_vec))))
    B = FFT(xn=np.array(x2_vec + [0] * (N - len(x2_vec))))
    C = A * B
    D = IFFT(xk=C)
    return calc_all_number(D)

# 直接使用numpy封装的FFT
def numpy_FFT_multiply(N, x1_vec, x2_vec):
    A = np.fft.fft(np.array(x1_vec + [0] * (N - len(x1_vec))))
    B = np.fft.fft(np.array(x2_vec + [0] * (N - len(x2_vec))))
    C = A * B
    D = np.fft.ifft(C)
    return calc_all_number(D)
    
if __name__ == '__main__':
    x1 = 12345670987281123213333123123213333333333333333331231231232123112132322101231233213333332131232131232132312312123213123123213214324323143243243231993146457656387648001273762153678236712763425461234567098728112321333312312321333333333333333333123123123212311213232210123123321333333213123213123213231231212321312312321321432432314324324323199314645765638764800127376215367823671276342546
    x2 = 99987654321066661267812333333333333333333333124324234234231231231212321314324243144354765786985654694385903412903498234712349882131323214837598743819023901281231231212395679498624356123123784287564102134285466673987654321066661267812333333333333333333333124324234234231231231212321314324243144354765786985654694385903412903498234712349882131323214837598743819023901281231231212395679498624356123123784287564102134285466673
    x1_vec = list(map(int, list(reversed(str(x1)))))
    x2_vec = list(map(int, list(reversed(str(x2)))))
    # 1、加倍次数界：由分治法的思想，将两个多项式的次数界补全为2的幂次
    extra_len = 1
    while 2**extra_len < len(x1_vec) + len(x2_vec):
        extra_len += 1
    N = 2**extra_len
    # 2、求值：通过FFT计算出两个多项式的点值表达
    # 3、逐点相乘：将两个多项式的点值依次相乘，得到相乘结果的点值
    # 4、插值：通过IDFT计算相乘结果的点值，得到相乘结果的每一个系数
    r1 = normal_multiply(N=N, x1_vec=x1_vec, x2_vec=x2_vec)  # 不使用矩阵乘法的离散傅里叶
    r2 = DFT_multiply(N=N, x1_vec=x1_vec, x2_vec=x2_vec)  # 使用矩阵乘法版本：DFT离散傅里叶变换
    r3 = FFT_multiply(N=N, x1_vec=x1_vec, x2_vec=x2_vec)  # 使用矩阵乘法版本：FFT快速傅里叶变换
    r4 = numpy_FFT_multiply(N=N, x1_vec=x1_vec, x2_vec=x2_vec)  # 直接使用numpy封装的FFT
    t1 = timeit('normal_multiply(N, x1_vec, x2_vec)', 'from __main__ import normal_multiply, N, x1_vec, x2_vec', number=1)
    t2 = timeit('DFT_multiply(N, x1_vec, x2_vec)', 'from __main__ import DFT_multiply, N, x1_vec, x2_vec', number=1)
    t3 = timeit('FFT_multiply(N, x1_vec, x2_vec)', 'from __main__ import FFT_multiply, N, x1_vec, x2_vec', number=1)
    t4 = timeit('numpy_FFT_multiply(N, x1_vec, x2_vec)', 'from __main__ import numpy_FFT_multiply, N, x1_vec, x2_vec', number=1)
    print(x1 * x2 == r1, x1 * x2 == r2, x1 * x2 == r3, x1 * x2 == r4)
    print('不使用矩阵乘法的离散傅里叶耗时：{}秒'.format(round(t1, 2)))
    print('使用矩阵乘法版本：DFT离散傅里叶变换耗时：{}秒'.format(round(t2, 2)))
    print('使用矩阵乘法版本：FFT快速傅里叶变换耗时：{}秒'.format(round(t3, 2)))
    print('直接使用numpy封装的FFT耗时：{}秒'.format(round(t4, 2)))
    print('结果比较：DFT提升{}倍计算速度，FFT提升{}倍计算速度，numpy FFT提升{}倍计算速度'.format(t1 // t2, t1 // t3, t1 // t4))
