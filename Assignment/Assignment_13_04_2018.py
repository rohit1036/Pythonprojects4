import csv
total=0
emp_num=0
with open('emp.csv','r')as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if "'IT'" in line:
           total+= int(line[2])
           emp_num+=1
avg_sal=total/emp_num
print("Avg salary of IT Department:",avg_sal)
print("Total number of employees working in IT Department:",emp_num)
