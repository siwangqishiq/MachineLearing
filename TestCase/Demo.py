from numpy import *;

print("This is my Test Case!!")


def testMat():
    m = mat([[1,2,3],
             [1,2,4],
             [3,2,5]])
    print(m)
    print(m.I)
    m2 = m * m.I
    print(m2)
    sum = m.sum(axis=0)
    print(sum)

testMat()