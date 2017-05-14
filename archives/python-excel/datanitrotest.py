import datetime
starttime = datetime.datetime.now()

CellRange('A1:ZZ1000').value = 1


endtime = datetime.datetime.now()

a = endtime-starttime

Cell('A1').value = a

a='00:21.0'