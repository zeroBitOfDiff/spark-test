# convert xml to json
import csv
import json
import os
userhome = os.path.expanduser('~')
csvFile = userhome + "/Projects/spark-test/test-csv/10681_2017_1876_MOESM1_ESM.csv"
jsonFile = userhome + "/Projects/spark-test/test-json/10681_2017_1876_MOESM1_ESM.json"

def conCSV2JSON(csvFile,jsonFile):
    data =[]
    with open(csvFile) as f: 
        reader = csv.DictReader(f)
        for rows in reader:
            # print(rows)
            # for key in rows:
            #     print(key)
            j = {}
            for key in rows:
                j[key] = rows[key]
            data.append(j)
            
    print(json.dumps(data, indent=4))

    with open(jsonFile, 'w') as jsonFile:

        jsonFile.write(json.dumps(data, indent=4))

def main():
    pass

if "__name__" == "__main__":
    main()
        
