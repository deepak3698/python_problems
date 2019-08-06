
'''
Problem statement 1:

A new organization has decided to base their company logo on the three most common characters in the company name. Given a string ,which is the company name, your task is to find the top three most common characters in the string. If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
    YAHOO would have its logo with the letters O, A, H
          ##Note the below points.
        1. The application will accept company ID as a input, fetch the name from JSON file, and will return company Id, company Name and logo characters as output.
         I/P : { company Name:"YAHOO"}
         O/P: { company Name:"YAHOO",logoCharacters:"O,A,H"}
        2. Use any familiar as your programming language.
Coding standards and code design should be followed and will be considered for assessment will along with logic and output.

'''

import json
from collections import Counter

with open('myjson.json') as data_file:
    data_item = json.load(data_file)["id"]

logo=[]

input_val=int(input("Please Enter Company id: "))
if(input_val==data_item['id_']):
    a=str(data_item['name'])
    count=Counter(a)
    a=dict(count)
    list1=[]
    list2=[]
    list3=[]
    for key,value in a.items():
        if(a[key]>1):
            list3.append(a[key])
            if(a[key]>max(list3)):
                list1.insert(0,key)
            else:
                list1.append(key)
        else:
            list2.append(key)
    list4=sorted(list1)+sorted(list2)
    dict1={'company_name':data_item['name'],'logo_char':list4[:3]}
    print(dict1)
else:
    print("Please  enter a valid id")