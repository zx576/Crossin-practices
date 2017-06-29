# http://paste.ubuntu.com/24955910/
# author:wuxiaojiao
# n=int(input("N:"))
n = 5
a=[[0 for i in range(1,n+1)]for j in range(1,n+1)]
x,y,i,j=0,0,0,0
while a[i][j]==0 :
        y+=1
        a[i][j]=y
        if j<n-1 and a[i][j+1]==0 and (i==0 or (i>0 and a[i-1][j]!=0 )):
        ##括号内容可保证第四个elif从下往上的顺序正常进行
            j+=1
        elif i<n-1 and a[i+1][j]==0:
            i+=1
        elif j>0 and a[i][j-1]==0:
            j-=1
        elif  i>0 and a[i-1][j]==0:
            i-=1
for row in a:
    for col in row:
        print(col, end=' ')

    print('\n')
