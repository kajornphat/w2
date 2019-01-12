import csv

file = 'TestCSV.csv'

def append(subject, credit, grade, semester):
	global file
	with open(file, 'a', newline = '') as csvfile:
		fieldnames = ['Subject', 'Credit', 'Grade', 'Semester']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'Subject': subject, 'Credit': credit, 'Grade' : grade, 'Semester': semester})

def insert():
	'''
	Display the input indication and show the recent input
	'''
	subject = str(input("Insert Subject : "))
	credit = input("Credit : ")
	grade = input("Grade : ")
	semester = input("Semester : ")
	append(subject, credit, grade, semester)
	
	recent_input = 'At semester '+semester+' you attend '+subject+'which has '+credit+' credits and you got '+grade+', has been added to csv files'
	print(recent_input)

def reader():
	global file
	with open(file, newline='') as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			print(row)

insert()