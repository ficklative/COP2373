# This program will open file grades.csv and will allow
# an instructor to enter an amount of students, then each
# students first and last name as strings,
# and three exam grades as integers.

# Import csv module
import csv

# Write the instructors input for student first and last name,
# and the totals for three exams for a given number of students
def main():
    # Variables
    students = 0
    first_name = 0
    last_name = 0
    exam1 = 0
    exam2 = 0
    exam3 = 0

    # Get amount of students from instructor
    try:
        students = int(input("Enter number of students: "))
        print('-' * 52)
        if students <= 0:
            print('Please enter a number greater than zero.')
    except ValueError:
        print("Please enter a number of students.")

    # Open or create grades.csv for writing
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        #create a header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Get input from instructor for each student
        for s in range(students):
            # Get input for the students first and last name
            print(f'Entering data for student number {s+1}')
            first_name = input("Enter your students first name: ").title()
            last_name = input("Enter your students last name: ").title()

            # Get input for exam1, exam2, and exam3
            exam1 = grade_validate(1)
            exam2 = grade_validate(2)
            exam3 = grade_validate(3)
            print('-' * 52)
            # Write each students first and last name, and the 3 exam scores
            # into a new row in the grades.csv file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Display that the data has been saved to grades.csv
    print('\nAll student data has been saved to grades.csv.'
          '\nTo view the data, open and run the grades.csv reader')

def grade_validate(exam):
    # Variables
    grade = 0

    # Validate the grade input as a positive int
    # between 0-100
    while True:
        try:
            grade = int(input(f"Enter your student's exam {exam} grade: "))
            if 0 <= grade <= 100:  # Ensure grade is valid
                return grade
            else:
                print("Please enter a grade between 0 and 100")
        # ValueError in case incorrect input is received
        except ValueError:
            print('invalid input. Please enter a numeric grade.')

# Call the main function
if __name__ == '__main__':
    main()