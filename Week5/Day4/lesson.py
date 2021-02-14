# with open ('blah.txt', 'w') as f:
#     f.write('Hello\n')

# with open('blah.txt', 'a') as f:
#     f.write('Goodbye') 

# with open('blah.txt', 'r') as f:        # opens file blah.txt
#     data = f.readlines()                # reads each line

# for person in data:  
#     person = person.strip('\n')                           # for loop the list
#     print(f'sending email to {person}')    # f-string to all lines

# w = write 
# r = read 
# a = append
# w+ = write + read 
# a+ = append + read 

# Writing...
# f.write()       = Writes a string to the file
# f.writelines()  = Writes a list to the file, line by line

# Reading... 
# f.read()      = Reads the enmtire file into a single string
# f.readline()  = read a single line
# f.readlines() = reads the entire file into a list of strings

#______________________________________________________  
# -------JSON---------
# import json

# load                     read json froma file and convert to python
# loads   S   string...... convert a json string to a python object

# dump                     convert from python to json and write to file 
# dumps                    convert from python to json string
# thing = [
#     {
#         'name' : 'bob',
#         'age' : 55
#     },                 
#     {
#         'nums': [1,2,3],
#         'letters': ['a','b','c']
#     },
# ]
# with open('jfile.txt', 'w') as f:
#     json.dump(thing, f, indent=3)

# with open('jfile.txt', 'r') as f: 
#     thing2 = json.load(f)
    
#______________________________________________________  
# ------- HTTPs ------- 
# HyperText Transfer Protocol (secure)

# url = Uniform Resource Locator

Get - requests (send the data you need in the url)
Post - 

#____________________________________________________________________

#--------API ---------- 

pip install requests 

import requests 
response = requests.get('url link here')
print(response)
