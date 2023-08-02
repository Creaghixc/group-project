import csv
import pandas as pd

# This function will print the student information to a .txt file 
def WriteToFile(data):

    with open('UIN.txt', 'a') as uin:
        uin.write(data+ '\n')

print("*******************Main Menu*****************")
print("1. Read CSV file of grades")
print("2. Generate student report file")
print("3. Generate student report charts")
print("4. Generate class report file")
print("5. Generate class report charts")
print("6. Quit")
print("************************************************")

# Option 1 read file 

'''with open ("grades.csv", 'r') as file:
    line = file.readline()
    while line != '':
        print(line)
        line = file.readline()
'''

# Option 2 get student information and print to a .txt file

with open('grades.csv', 'r') as file:
    lines = csv.DictReader(file)
    # uin = input("Enter the uin: ")
    for row in lines:
        print(row['UIN'])
    
    
