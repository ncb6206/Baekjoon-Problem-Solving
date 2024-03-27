import sys

gradeSet = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

hap,count = 0,0

for _ in range(20):
    subject, credit, grade = map(str,sys.stdin.readline().split())
    if(grade == 'P'):
        continue
    hap += float(credit) * gradeSet[grade]

    count += float(credit)

print("{:.6f}".format(hap/count))