# convert xml to json
import csv
import json
import os


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
            
    #print(json.dumps(data, indent=4))

    with open(jsonFile, 'w') as jsonFile:

        jsonFile.write(json.dumps(data, indent=4))

def breakUpJson(jsonFile,jsonFile2):
    listOfJson = []
    newListOfJson = []
    with open(jsonFile) as jf:
        listOfJson = json.loads(jf.read())
        print(len(listOfJson))
        for item in listOfJson:
            newListOfJson.append(json.dumps(item) + '\n')
    with open(jsonFile2, 'w') as jsonFile:
        jsonFile.write(json.dumps(newListOfJson))
# next line after each json file

def viewJson(jsonFile):
    with open(jsonFile) as j:
        jf = json.loads(j.read())
        print(json.dumps (jf, indent=4))
    

def main():
    userhome = os.path.expanduser('~')
    
    j = userhome + "/Projects/spark-test/test-json/10681_2017_1876_MOESM1_ESM.json"
    j2 = userhome + "/Projects/spark-test/test-json/t2.json"
    print(j)
    # breakUpJson(j,j2)
    viewJson(j2)
    

if __name__ == '__main__':
    main()
        
