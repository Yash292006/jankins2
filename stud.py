# Student details program using lists

students = [
    {
        "name": "John Doe",
        "roll": "101",
        "marks": [85.0, 92.0, 78.0]
    },
    {
        "name": "Jane Smith", 
        "roll": "102",
        "marks": [95.0, 88.0, 92.0]
    }
]

for i, student in enumerate(students, 1):
    name = student["name"]
    roll = student["roll"]
    marks = student["marks"]
    
    total = sum(marks)
    avg = total / len(marks)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "Fail"
    
    print(f"\nStudent {i} Details:")
    print(f"Name: {name}")
    print(f"Roll No: {roll}")
    print(f"Total: {total:.2f}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")