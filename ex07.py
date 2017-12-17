# 7.define a function diaginal_reverse() that takes matrix and returns diagonal-reversed one:
#1 2 3         1 4 7
#4 5 6 returns 2 5 8
#7 8 9         3 6 9
#m = [[1,2,3],[4,5,6],[7,8,9]]

def rotate(m):
    rm = []
    for i in range(0,len(m)):
            rm.append([row[i] for row in m])           
    return rm 
#rm = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
