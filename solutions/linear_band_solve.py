from matplotlib import pyplot as plt
import numpy as np

# 定义 N = 20
n = 20
v = 2


def linear_gap_calculation(k):
    '''
    线性带的计算，k 为参数
    超参数 n = 20
    V(x) = vcos(x)
    TODO 需要将这个方法变成支持 a * con(sin)(m * x) + b * cos(sin)(n * x)
    TODO 写一个函数解析任意类型的三角函数
    '''
    diag_mx = np.arange(-n, n+1, 1)
    a = np.ones((2 * n + 1))
    # 构造出矩阵形式
    H = np.diag(0.5 * (diag_mx ** 2 + 2 * diag_mx * k + a * k ** 2))+ \
            np.diag(np.ones((2 * n)) * v / 2, 1) + np.diag(np.ones((2 * n)) * v / 2, -1)
    eig_value, eig_v = np.linalg.eig(H)
    return eig_value, eig_v

def gnrt_linear_graph():
    x = np.linspace(-0.5, 0.5, 100)
    value_lst = np.array([linear_gap_calculation(i)[0] for i in x]).T
    value_lst.sort(0)
    for i in value_lst[:4]:
        #print(i)
        plt.plot(x, i, 'g-')
    plt.show()
    return value_lst

a = gnrt_linear_graph()
