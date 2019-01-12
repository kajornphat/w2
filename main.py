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

def calculateGPA(semester):
	grade = {'A': 4, 'B+': 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D+': 1.5, 'D': 1, 'F': 0}
	sum_point = 0
	sum_credit = 0
	global file
	with open(file, newline='') as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			if row['Semester'] == str(semester):
				point = int(row['Credit']) * grade[row['Grade']]
				sum_point += point
				sum_credit += int(row['Credit'])
		return sum_point/sum_credit

print(calculateGPA(2))