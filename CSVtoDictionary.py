import csv

dic = {}

with open('List of all subdistricts - Sheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[0], row[1], row[2])
            stateName = row[0].title()
            districtName = row[1].title()
            subDistrictName = row[2].title()
            if stateName not in dic.keys():
                dic[stateName] = {}
            if districtName not in dic[stateName].keys():
                dic[stateName][districtName] = []
            dic[stateName][districtName].append(subDistrictName)
            line_count += 1
    print(f'Processed {line_count} lines.')
dic = str(dic)

try: 
    geeky_file = open('PythonDictionary.txt', 'wt') 
    geeky_file.write(dic) 
    geeky_file.close() 
  
except: 
    print("Unable to write to file")