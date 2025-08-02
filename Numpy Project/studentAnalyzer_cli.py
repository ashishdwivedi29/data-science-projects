# student_analyzer_cli.py

import numpy as np
from numpy.linalg import det, inv

def input_data():
    num_students = int(input("Enter number of students: "))
    num_subjects = int(input("Enter number of subjects: "))

    students = [input(f"Student {i+1} name: ") for i in range(num_students)]
    subjects = [input(f"Subject {i+1} name: ") for i in range(num_subjects)]

    marks = np.zeros((num_students, num_subjects), dtype=int)
    print("\nEnter marks for each student:")
    for i in range(num_students):
        print(f"--- {students[i]}'s marks ---")
        for j in range(num_subjects):
            marks[i][j] = int(input(f"Marks in {subjects[j]}: "))

    return np.array(students), np.array(subjects), marks

def basic_analytics(students, subjects, marks):
    total_marks = marks.sum(axis=1)
    average_marks = marks.mean(axis=1)
    max_marks = marks.max(axis=1)
    min_marks = marks.min(axis=1)

    print("\nTotal Marks:")
    for i in range(len(students)):
        print(f"{students[i]}: {total_marks[i]}")

    print("\nAverage Marks:")
    for i in range(len(students)):
        print(f"{students[i]}: {round(average_marks[i], 2)}")

    print("\nMaximum Marks:")
    for i in range(len(students)):
        print(f"{students[i]}: {max_marks[i]}")

    print("\nMinimum Marks:")
    for i in range(len(students)):
        print(f"{students[i]}: {min_marks[i]}")

    class_avg = marks.mean(axis=0)
    std_dev = marks.std(axis=0)
    subject_max = marks.max(axis=0)
    subject_min = marks.min(axis=0)

    print("\nClass Average per Subject:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {round(class_avg[i], 2)}")

    print("\nStandard Deviation:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {round(std_dev[i], 2)}")

    print("\nMaximum per Subject:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {subject_max[i]}")

    print("\nMinimum per Subject:")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {subject_min[i]}")

def student_ranking(students, marks):
    total_marks = marks.sum(axis=1)
    sorted_indices = np.argsort(total_marks)[::-1]
    ranked_students = students[sorted_indices]
    ranked_totals = total_marks[sorted_indices]

    ranks = np.empty_like(sorted_indices)
    rank = 1
    for i in range(len(sorted_indices)):
        if i > 0 and ranked_totals[i] == ranked_totals[i-1]:
            ranks[i] = ranks[i-1]
        else:
            ranks[i] = rank
        rank += 1

    print("\nStudent Rankings:")
    for i in range(len(students)):
        print(f"Rank {int(ranks[i])}: {ranked_students[i]} - {ranked_totals[i]} marks")

def subject_analysis(students, subjects, marks):
    print("\nTopper in Each Subject:")
    for i in range(len(subjects)):
        max_score = marks[:, i].max()
        toppers = students[marks[:, i] == max_score]
        print(f"{subjects[i]}: {', '.join(toppers)} with {max_score} marks")

    print("\nStudents Below Average in Each Subject:")
    avg = marks.mean(axis=0)
    for i in range(len(subjects)):
        below = students[marks[:, i] < avg[i]]
        print(f"{subjects[i]}: {', '.join(below) if below.size > 0 else 'None'}")

def matrix_operations(marks):
    print("\nMatrix Transformations:")
    print("Transposed:\n", marks.T)
    print("Flattened:\n", marks.flatten())
    print("Raveled:\n", marks.ravel())
    reshaped = marks.reshape(1, marks.shape[0], marks.shape[1])
    print("Reshaped:\n", reshaped)
    resized = np.resize(marks, (marks.shape[0], marks.shape[1] + 1))
    print("Resized:\n", resized)
    print("Swapped Axes:\n", np.swapaxes(marks, 0, 1))
    print("Flattened and Reshaped:\n", marks.flatten().reshape(marks.shape[0], marks.shape[1]))

def weighted_scores(students, subjects, marks):
    weights = np.array([float(input(f"Enter weight for {s} (%): ")) for s in subjects])
    if weights.sum() != 100:
        print("Normalizing weights...")
    weights /= 100
    scores = np.dot(marks, weights)
    print("\nWeighted Scores:")
    for i in range(len(students)):
        print(f"{students[i]}: {scores[i]:.2f}")

def advanced_queries(students, subjects, marks):
    if "Math" in subjects and "English" in subjects:
        math_idx = np.where(subjects == "Math")[0][0]
        eng_idx = np.where(subjects == "English")[0][0]

        math_90 = students[marks[:, math_idx] >= 90]
        both_90 = students[(marks[:, math_idx] >= 90) & (marks[:, eng_idx] >= 90)]

        print("\n90+ in Math:", math_90 if math_90.size else "None")
        print("90+ in Math & English:", both_90 if both_90.size else "None")

    low_scorers = np.unique(np.where(marks < 50)[0])
    print("\n<50 in any subject:", students[low_scorers] if low_scorers.size else "None")

    sub = input("\nEnter subject for custom filter: ")
    if sub in subjects:
        idx = np.where(subjects == sub)[0][0]
        threshold = int(input(f"Threshold for {sub}: "))
        filtered = students[marks[:, idx] >= threshold]
        print(f">= {threshold} in {sub}: {filtered if filtered.size else 'None'}")
    else:
        print("Subject not found!")

def main():
    students, subjects, marks = input_data()

    while True:
        print("""
========= MENU =========
1. Basic Analytics
2. Student Ranking
3. Subject-Wise Analysis
4. Matrix Operations
5. Weighted Scores
6. Advanced Queries
7. Exit
========================
""")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            basic_analytics(students, subjects, marks)
        elif choice == '2':
            student_ranking(students, marks)
        elif choice == '3':
            subject_analysis(students, subjects, marks)
        elif choice == '4':
            matrix_operations(marks)
        elif choice == '5':
            weighted_scores(students, subjects, marks)
        elif choice == '6':
            advanced_queries(students, subjects, marks)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
