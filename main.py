# Main Program Outline I'm using to test
# So far Options 3,4 and 6 have functionality
from ebo_functions import generate_student_report_charts, generate_class_report

prog_switch = 1
while prog_switch == 1:
    print(f"{'*'*19}Main Menu{'*'*17}")
    print("1. Read CSV file of grades")
    print("2. Generate student report file")
    print("3. Generate student report charts")
    print("4. Generate class report file")
    print("5. Generate class report charts")
    print("6. Quit")
    
    user_option = int(input("Enter an option number: "))
    
    if user_option == 1:
        pass
    elif user_option == 2:
        pass
    elif user_option == 3:
        report_uin = input("Enter a UIN to generate a report for: ")
        generate_student_report_charts(report_uin, "grades.csv")
    elif user_option == 4:
        generate_class_report("grades.csv")
    elif user_option == 5:
        pass
    elif user_option == 6:
        # Ends the loop
        prog_switch = 0
    else:
        print("Input not recognized, please try again.")