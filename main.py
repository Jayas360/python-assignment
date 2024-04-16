import requests 
from bs4 import BeautifulSoup
import db
import csv
  
# making a GET request 
r = requests.get('https://www.practo.com/tests?city=delhi') 
  
# parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

# selecting elements with given class name 
tests = soup.select('.slick-active')

test_list = []

for test in tests : 
    # selecting targeted nested div content
    curr = test.select('div>div>div>a>div');

    # no. of elements with in current div
    childCount = len(curr)

    # filtering incomplete test data
    if childCount != 4 :
        continue
    cur_test = (curr[0].text, curr[1].text, curr[2].text, curr[3].text[1:])
    test_list.append(cur_test);

# creating table to store test data
db.create()

# adding data to the table
db.deleteAll()
for test in test_list:
    db.insert(test)

# fetching data from table 
data = db.fetch()
# print(data)

# field names for csv file storage
fields = ['test_name', 'test_desc', 'test_report', 'cost']

# name of the csv file
filename = "test_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile : 
    #creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the rows
    for test in data:
        csvwriter.writerow([test[0], test[1], test[2], test[3]]) 
