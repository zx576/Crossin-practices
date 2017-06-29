# https://paste.ubuntu.com/24931259/
# 成仙

import numpy as np

def SpiralMat(degree):
    dire = np.array([[0,1],[1,0],[0,-1],[-1,0]])
    mat = np.zeros((degree,degree))
    currentaxis = (0,0)
    turnsign = 0

    for step in range(degree**2):
        #print('{0},{1}'.format(step+1,currentaxis))
        mat[tuple(currentaxis)] = step+1

        tmp = currentaxis + dire[turnsign]

        if (tmp[0] > degree-1) or (tmp[1] > degree-1) or (mat[tuple(tmp)] != 0):
            turnsign += 1

        if turnsign > 3:
            turnsign = 0

        currentaxis += dire[turnsign]
    return mat


def ValuePrint(mat):
    x = mat.shape[0]
    #y = mat.shape[1]

    for lx in range(x):
        l = mat[lx,:]
        print(l[0:x])

    print('Done!')


def main():
    degree = input('Tell me the degree!\n')

    mat = SpiralMat(int(degree))

    ValuePrint(mat)

if __name__=="__main__":
    main()
