import csv
with open("test.cs",'w',newline='') as f :
    csvwriter=csv.writer(f)
    data=[['stocks','sales'],
          ['100','24'],
          ['50','12'],
          ['30','4']]
    csvwriter.writerows(data)

