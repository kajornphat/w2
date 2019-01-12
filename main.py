import csv

def append(subject, credit, grade):
    with open('TestCSV.csv', 'a', newline = '') as csvfile:
        fieldnames = ['Subject', 'Credit', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Subject': subject, 'Credit': credit, 'Grade' : grade})

def insert():
    '''
    Display the input indication and show the recent input
    '''
    subject = input("Insert Subject : ")
    credit = input("Credit : ")
    grade = input("Grade : ")
    
    append(subject, credit, grade)
    
    recent_input = subject + ' has ' + credit + ' credits and you got ' + grade + ', has been added to csv files'
    
    print(recent_input)

insert()
