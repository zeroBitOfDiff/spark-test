# convert xml to json
import csv
import json
import os
userhome = os.path.expanduser('~')
csvFile = userhome + "/Projects/spark-test/test-csv/10681_2017_1876_MOESM1_ESM.csv"

with open(csvFile) as f: 
    reader = csv.DictReader(f)
    for rows in reader:
        # print(rows)
        # for key in rows:
        #     print(key)
        for key in rows:
            print(rows[key])
        break
        
