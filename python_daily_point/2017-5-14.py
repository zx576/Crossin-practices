import csv

with open('test.csv','w')as f:
    wt = csv.writer(f)
    for i in range(5):
        wt.writerow([str(i),str(i+1)])
