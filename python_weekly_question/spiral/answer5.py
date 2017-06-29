# https://paste.ubuntu.com/24932920/
# SFFL

from __future__ import division

cont=True
while cont==True:
    dim=input('Please enter an integer as the dimension of this matrix: ')
    dim=int(dim)

    if dim==1 or dim==0:
        print(dim)

    else:
        layers=0
        core=0
        tot=dim**2
        x=0
        y=0
        prt_list=[0]*tot

        if dim%2==0:
            layers=int(dim/2)
        else:
            layers=int((dim-1)/2)
            core=1

        for i in range(1,tot+1):
            if i==tot and core==1:
                x=layers+1
                y=layers+1
            else:
                tmp=i
                k=0
                for j in range(0,layers):
                    tmp=tmp-(dim-1-j*2)*4
                    k+=1
                    if tmp<=0:
                        tmp=tmp+(dim-1-j*2)*4
                        break

                layer_size=(dim-1-(k-1)*2)*4
                quad=tmp/layer_size
                if 0<quad<=0.25:
                    x=k
                    y=k+(tmp-1)
                elif 0.25<quad<=0.5:
                    x=k+(tmp-0.25*layer_size-1)
                    y=dim-(k-1)
                elif 0.5<quad<=0.75:
                    x=dim-(k-1)
                    y=(dim-(k-1))-(tmp-0.5*layer_size-1)
                elif 0.75<quad<=1:
                    x=dim-(k-1)-(tmp-0.75*layer_size-1)
                    y=k

            prt_order=int((x-1)*dim+y)
            prt_list[prt_order-1]=i

        pointer=0
        for ii in range(0,dim):
            for jj in range(0,dim):
                print('%d\t'%prt_list[pointer], end=' ')
                pointer+=1
            print('\n')

    c=input('Continue(y/n)? ')
    if c=='y':
        continue
    else:
        cont=False
