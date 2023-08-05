import csv

# Option 1 read file 
def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = csv.reader(file)

# Option 2 get student information and write to a .txt file 
def check_uin(uin):
    # Checks the validity of the uin
    if (len(uin) == 10) and (uin.isnumeric()==True):
        valid_uin = True
    else:
        valid_uin = False
    return valid_uin
    
def generate_student_report(grade_file):
    # Calculates the students grade report
    with open(grade_file, newline='') as file:
        reader = csv.reader(file)
        csvFile = list(reader)
        
        # Checks the validity of the uin and loops if not valid until user enters a valid uin
        uin = input("Enter the uin: ")
        valid_uin = check_uin(uin)
        while valid_uin == False:
            uin = input("Enter the uin: ")
            valid_uin = check_uin(uin)
            
        for row in csvFile:
            if row[0] == uin:
                # Exams and Exam means
                exam1 = float(row[19])
                exam2 = float(row[20])
                exam3 = float(row[21])
                exam_mean = round((exam1 + exam2 + exam3)/3,2)
                
                # Lab and Lab means
                lab1 = float(row[1])
                lab2 = float(row[2])
                lab3 = float(row[3])
                lab4 = float(row[4])
                lab5 = float(row[5])
                lab6 = float(row[6])
                lab_means = round(((lab1 + lab2 + lab3 + lab4 + lab5 + lab6)/6),2)
                
                # Quiz and Quiz means
                quiz1 = float(row[7])
                quiz2 = float(row[8])
                quiz3 = float(row[9])
                quiz4 = float(row[10])
                quiz5 = float(row[11])
                quiz6 = float(row[12])
                quiz_means = round(((quiz1 + quiz2 + quiz3 + quiz4 + quiz5 + quiz6)/6),2)
                
                # Reading and Reading means
                reading1 = float(row[13])
                reading2 = float(row[14])
                reading3 = float(row[15])
                reading4 = float(row[16])
                reading5 = float(row[17])
                reading6 = float(row[18])
                reading_means = round(((reading1 + reading2 + reading3 + reading4 + reading5 + reading6)/6),2)
                
                # Project
                project = float(row[22])
                
                # Calculates the student's total score for the class
                score = round(((exam_mean * .45) + (lab_means * .25) + (quiz_means * .10) + (reading_means * .10) + (project * .10)),2)
                
                # Calculates the letter grade
                if score >= 90:
                    letter_grade = 'A'
                elif 80 <= score > 90:
                    letter_grade = 'B'
                elif 70 <= score > 80:
                    letter_grade = 'C'
                elif 60 <= score > 70:
                    letter_grade = 'D'
                else:
                    letter_grade = 'F'
                
                with open("UIN.txt", 'w') as student_report:
                    student_report.write(f"Exams mean: {exam_mean}\n")
                    student_report.write(f"Labs mean: {lab_means}\n")
                    student_report.write(f"Quizzes mean: {quiz_means}\n")
                    student_report.write(f"Reading activities mean: {reading_means}\n")
                    student_report.write(f"Score: {score}\n")
                    student_report.write(f"Letter grade: {letter_grade}\n")
                student_report.close()
                            
            
    
    
    
