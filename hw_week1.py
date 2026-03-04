import numpy as np

# Exercise 1.4
def conv2d(X, W, S, P):
    X = zero_padding(X, P)
    os = int( np.floor( (X.shape[0]-W.shape[0]) / S ) + 1 )
    O = np.zeros((os,os))
    for ii in range(os):
        for jj in range(os):
            tmp = 0
            for u in range(W.shape[0]):
                for v in range(W.shape[1]):
                    tmp = tmp + X[ii*S+u, jj*S+v]*W[u,v]
            O[ii, jj] = tmp
    return O

def zero_padding(x, p):
    u,v = x.shape
    out = np.zeros((u+2*p, v+2*p))
    for ii in range(p):
        out[0:p, :] = np.zeros((p, v+2*p))
        out[u+p:u+2*p, :] = np.zeros((p, v+2*p))
        out[p:u+p, 0:p] = np.zeros((u, p))
        out[p:u+p, v+p:v+2*p] = np.zeros((u, p))
    out[p:p+u, p:p+v] = x

    return out

def max_pooling(X, S):
    ui, vi = X.shape
    uo, vo = ui//S, vi//S
    out = np.zeros((uo, vo))
    for ii in range(uo):
        for jj in range(vo):
            patch = X[ii*S:ii*S+S, jj*S:jj*S+S]
            out[ii, jj] = patch.max()
    return out

def avg_pooling(X, S):
    ui, vi = X.shape
    uo, vo = ui//S, vi//S
    out = np.zeros((uo, vo))
    for ii in range(uo):
        for jj in range(vo):
            patch = X[ii*S:ii*S+S, jj*S:jj*S+S]
            out[ii, jj] = patch.mean()
    return out

# Exercise 1.4 (a)
print("Exercise 1.4 (a):")
X = np.array([[1.23, 0.94, 0.83, 0.2], [0.34, 0.44, 0.37, 0.3],
              [0.34, 1.14, 2.34, 1.24], [0.49, 0.18, 2.04, 1.42]])
W = np.array([ [1, 0.5], [0.3, 1] ])
S, P = 1, 0
O = conv2d(X, W, S, P); print(O)
S, P = 2, 0
O = conv2d(X, W, S, P); print(O)

# Exercise 1.4 (b)
print("Exercise 1.4 (b):")
S, P = 1, 1
O1 = conv2d(X, W, S, P); print(O1)
S, P = 2, 1
O2 = conv2d(X, W, S, P); print(O2)
om = max_pooling(O1, 2); print(om)
oa = avg_pooling(O1, 2); print(oa)

# Exercise 1.4 (c)
print("Exercise 1.4 (c):")
R = np.array([[123, 94, 83], [34, 44, 37], [34, 114, 234]])
G = np.array([[123, 94, 20], [11, 30, 22], [12, 40, 23]])
B = np.array([[123, 94, 83], [34, 44, 37], [34, 114, 234]])
W1 = np.array([[1, 0.5], [0.3, 1]])
W2 = np.array([[0.5, 1], [1, 0.3]])
O1R = conv2d(R, W1, 1, 1)
O1G = conv2d(G, W1, 1, 1)
O1B = conv2d(B, W1, 1, 1)
print(O1R+O1G+O1B)
O2R = conv2d(R, W2, 1, 1)
O2G = conv2d(G, W2, 1, 1)
O2B = conv2d(B, W2, 1, 1)
print(O2R+O2G+O2B)