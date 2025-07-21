import numpy as np

def main():
    # Load the exam grades from grades.csv
    data = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, usecols=(2, 3, 4))

    # Print the data in an array
    print(data)
    calculate(data)

# Use numpy to calculate data
def calculate(data):
    # Label each column
    exam_labels = ['Exam 1', 'Exam 2', 'Exam 3']

    # Calculate for each exam column
    try:
        for i in range(data.shape[1]):
            exam_scores = data[:,i]

            # Calculate the mean, median, standard deviation, max, and min
            print(f"\nStats for {exam_labels[i]}:")
            print(f"  Mean:   {np.mean(data[:, i]):.2f}")
            print(f"  Median: {np.median(data[:, i]):.2f}")
            print(f"  Std:    {np.std(data[:, i]):.2f}")
            print(f"  Max:    {np.max(data[:, i]):.2f}")
            print(f"  Min:    {np.min(data[:, i]):.2f}")

            # Calculate pass or fail
            passing = np.sum(exam_scores >= 60)
            failing = np.sum(exam_scores < 60)

            # Display pass or fail
            print(f"  Passing: {passing}")
            print(f"  Failing: {failing}")

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("File contains invalid data or non-numeric exam scores")

if __name__ == '__main__':
    main()