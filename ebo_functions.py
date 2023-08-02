# A file for all my functions, just for organization
# Can either be imported or copy-pasted

import csv
import matplotlib.pyplot as plt
import os

# Option 3 Function
# file_rows[x][0] : UIN
# file_rows[x][1] - file_rows[x][6] : Labs 1 through 6
# file_rows[x][7] - file_rows[x][12] : Quiz 1 through 6
# file_rows[x][13] - file_rows[x][18] : Reading 1 through 6
# file_rows[x][19] - file_rows[x][21] : Exams 1 through 3
# file_rows[x][22] : Project
# Known issues : Saving the figures appends the new bar graphs to each preceeding figure so only the exam chart is really correct

def generate_student_report_charts(uin, grade_file):
    with open(grade_file, 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
    
        file_rows = []
        for line1 in file_reader:
            file_rows.append(line1)
        
        for line2 in range(len(file_rows)):
            if uin in file_rows[line2]:
                student_info = line2
                # print(f"Found at line {line2}")
        
        # print(file_rows[student_info])
        
        # Anything that creates a file or directory in this function is commented out right now
        # See Lines 34, 42, 51, 60, and 69
        # os.mkdir(uin)
        
        # Exam Bar Chart
        exams = [float(exam) for exam in file_rows[student_info][19:22]]
        
        exam_bar = plt.bar(file_rows[0][19:22], exams, align='center')
        plt.yticks(range(0,110,10))
        plt.title(f"{uin} CSCE 110 Exam Grades")
        #plt.savefig(os.path.join(uin, "exam_bar.png"))
        plt.show()
        
        # Lab Bar Chart
        labs = [float(lab) for lab in file_rows[student_info][1:7]]
        
        lab_bar = plt.bar(file_rows[0][1:7], labs, align='center')
        plt.yticks(range(0,110,10))
        plt.title(f"{uin} CSCE 110 Lab Grades")
        #plt.savefig(os.path.join(uin, "lab_bar.png"))
        plt.show()
        
        # Quiz Bar Chart
        quizzes = [float(quiz) for quiz in file_rows[student_info][7:13]]
        
        quizes_bar = plt.bar(file_rows[0][7:13], quizzes, align='center')
        plt.yticks(range(0,110,10))
        plt.title(f"{uin} CSCE 110 Quiz Grades")
        #plt.savefig(os.path.join(uin, "quiz_bar.png"))
        plt.show()
        
        # Reading Bar Chart
        readings = [float(reading) for reading in file_rows[student_info][13:19]]
        
        readings_bar = plt.bar(file_rows[0][13:19], readings, align='center')
        plt.yticks(range(0,110,10))
        plt.title(f"{uin} CSCE 110 Reading Grades")
        #plt.savefig(os.path.join(uin, "reading.png"))
        plt.show()
        
        
# Option 4 Function
# Works perfectly as far as I'm aware
def generate_class_report(grade_file):
    with open(grade_file, 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
    
        file_rows = []
        for line1 in file_reader:
            file_rows.append(line1)
        
        # Total Number of Students
        num_students = len(file_rows) - 1
        
        averages = []
        
        for student in range(1, len(file_rows)):
            exam1 = float(file_rows[student][19])
            exam2 = float(file_rows[student][20])
            exam3 = float(file_rows[student][21])
            
            lab_grades = [float(lab) for lab in file_rows[student][1:7]]
            lab_average = sum(lab_grades) / 6
            
            quiz_grades = [float(quiz) for quiz in file_rows[student][7:13]]
            quiz_average = sum(quiz_grades) / 6
            
            reading_grades = [float(reading) for reading in file_rows[student][13:19]]
            reading_average = sum(reading_grades) / 6
            
            project = float(file_rows[student][22])
            
            student_average = (exam1 * 0.15) + (exam2 * 0.15) + (exam3 * 0.15) + (lab_average * 0.25) + (quiz_average * 0.10) + (reading_average * 0.10) + (project * 0.10)
            averages.append(student_average)
        
        # Minimum Score
        score_min = min(averages)
        
        # Maximum Score
        score_max = max(averages)
        
        # Median Score
        ordered_averages = averages
        ordered_averages.sort()
        
        # print(len(ordered_averages))
        
        # ordered_averages = [1,2,3,4,5]
        # print("LENGTH", len(ordered_averages))
        
        if len(ordered_averages) % 2 == 0:
            # print("MID INDEX WHEN EVEN", int((len(ordered_averages)) / 2))
            
            mid_index = int(((len(ordered_averages)) / 2))
            score_median = (ordered_averages[mid_index] + ordered_averages[mid_index-1]) / 2
        else:
            # print("MID INDEX WHEN ODD", int((len(ordered_averages)-1) / 2))
            
            mid_index = int(((len(ordered_averages)-1) / 2))
            
            score_median = ordered_averages[mid_index]
            
        # print(score_median)
        
        # Mean Score
        score_mean = sum(averages) / len(averages)
        
        # Standard Deviation
        score_std_dev = 0
        
        std_dev_top = 0
        for num in averages:
            std_dev_top += pow((num - score_mean), 2)
            
        score_std_dev = pow((std_dev_top / len(averages)), (1/2))
        
    with open("report.txt", 'w') as report:
        report.write(f"Total number of students: {num_students}\n")
        report.write(f"Minimum score: {score_min}\n")
        report.write(f"Maximum score: {score_max}\n")
        report.write(f"Median score: {score_median}\n")
        report.write(f"Mean score: {score_mean}\n")
        report.write(f"Standard deviation: {score_std_dev}\n")