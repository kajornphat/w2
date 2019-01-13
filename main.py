import csv
import shutil

file = 'Grade/Database To-Do Week 1 GPA - Sheet1.csv'

def get_length(file_path):
	with open(file_path, "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)

def append(subject, credit, grade, semester):
	global file
	with open(file, 'a', newline = '') as csvfile:
		fieldnames = ['id', 'Subject', 'Credit', 'Grade', 'Semester']
		next_id = get_length(file)
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({
					'id' : next_id,
					'Subject': subject, 
					'Credit': credit, 
					'Grade' : grade, 
					'Semester': semester
					})

def insert():
	'''
	Display the input indication and show the recent input
	'''
	subject = str(input("Insert Subject : "))
	credit = input("Credit : ")
	grade = input("Grade : ")
	semester = input("Semester : ")

	recent_input = 'At semester '+semester+' you attend '+subject+' which has '+credit+' credits and you got '+grade+', has been added to csv files'
	print(recent_input)
	return subject, credit, grade, semester

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
				# print(row)
		return sum_point/sum_credit

def edit(edit_id, subject, credit, grade, semester):
	global file
	with open(file, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		with open('temp_file.csv', "w") as temp_file:
			fieldnames = ['id', 'Subject', 'Credit', 'Grade', 'Semester']
			writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
			writer.writeheader()
			for row in reader:
				if edit_id is not None:
					if row['id'] == str(edit_id):
						row['Subject'] = subject
						row['Credit'] = credit
						row['Grade'] = grade
						row['Semester'] = semester
				else:
					pass
				writer.writerow(row)

	shutil.move('temp_file.csv', file)

def text_modeUI():
	user_input = input('Press "I" to insert your grade, "E" to edit the selected data, "C" to calculate GPA, "Z" to exit\nEnter : ')
	return user_input

def csvlist(selected = None):
	global file	
	with open(file, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		if selected is not None:
			for row in reader:
				if row['id'] == str(selected):
					print("You choose "+row['Subject']+', Credit '+row['Credit']+', Grade '+row['Grade']+', Semester '+row['Semester'])
		else:
			print("List of Subjects in CSV file")
			for row in reader:		
				print(row['id']+'. '+row['Subject'])

if __name__ == '__main__':
	print("'Your GPA system'\nWhere you can edit/insert/save your grade into CSV file")
	while(1):
		user_input = text_modeUI()
		if user_input in ['I','i']:
			subject, credit, grade, semester = insert()
			append(subject, credit, grade, semester)
		
		elif user_input in ['E','e']:
			csvlist()
			input_id = input("Which subject you wish to change (insert an id) : ")
			csvlist(input_id)
			subject, credit, grade, semester = insert()
			edit(input_id, subject, credit, grade, semester)

		elif user_input in ['C','c']:
			select_semester = input("Select the semester : ")
			print(calculateGPA(select_semester))
		
		elif user_input in ['Z','z']:
			print("Good bye!")
			break
		