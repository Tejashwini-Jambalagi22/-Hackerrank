'''Project – Version 1

Create a Python program to manage student marks using lists.


Requirements:
1. Store five student marks in a list.
2. Display all marks.
3. Calculate total marks.
4. Calculate average marks.
5. Find the highest and lowest marks.
6. Count how many students passed (marks at least 40).'''


marks = [85, 70, 35, 90, 60]

total = sum(marks)
average = total / len(marks)

highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

print("Student Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)