import csv

def main():
    with open('grades.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        print(f"{'First Name':<12} {'Last Name':<12} {'Exam 1':<8} {'Exam 2':<8} {'Exam 3':<8}")
        print("-" * 52)

        next(reader)

        for row in reader:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

if __name__ == "__main__":
    main()