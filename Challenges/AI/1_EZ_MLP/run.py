import numpy as np

def fc(x, weight, bias):
    return np.matmul(x, weight) + bias

def forward(x):
    z1 = fc(x, w1, b1)
    z2 = fc(z1, w2, b2)
    y = fc(z2, w3, b3)
    return y

w1 = np.load('npys/w1.npy')
b1 = np.load('npys/b1.npy')
w2 = np.load('npys/w2.npy')
b2 = np.load('npys/b2.npy')
w3 = np.load('npys/w3.npy')
b3 = np.load('npys/b3.npy')

float2chr = lambda f: chr(int(np.round((f + 1) * 255 / 2)))

inputs = np.load('npys/inputs.npy')
flag = ''
for i in range(len(inputs)):
    y = forward(inputs[i])
    c0 = float2chr(y[0, 0])
    c1 = float2chr(y[1, 0])
    flag += c0 + c1
print('moectf{' + flag + '}')

# Hints:
#  > Fix the bug in the code to get the flag, only one line of code needs to be changed.
#  > Understand the code and the figure(Example.jpg) before flag submission.
#  > Example.jpg is only for tutorial and demonstration, no hidden information contained.