with open('aaa.txt','r') as f:
    steps = 20
    text = f.readlines()
    startnum = 0
    endnum = len(text)
    filenum = 1
    for num in range(startnum, endnum):
        if endnum == startnum:
            break
        elif endnum - startnum >= steps:
            step = steps
        else:
            step = endnum-startnum
        filename = 'a'+str(filenum)
        with open('%s.txt'%(filename),'w') as m:
            for v in range(step):
                m.write(text[startnum])
                startnum += 1
        filenum +=1

