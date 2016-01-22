import numpy as np


def softmax(x):
    e = np.exp(x)
    d = e/np.sum(e, axis=0)
    return  d

if __name__ == '__main__':
    w_1 = np.array([5.0, 1.0, 0.1])
    print softmax(w_1)

    w_2 = np.array([-1.0, 4.0, 0.1])
    print softmax(w_2)