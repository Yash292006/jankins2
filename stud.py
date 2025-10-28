# ...existing code...
# Basic student details program

name = input("Name: ")
roll = input("Roll No: ")

m1 = float(input("Marks subject 1: "))
m2 = float(input("Marks subject 2: "))
m3 = float(input("Marks subject 3: "))

total = m1 + m2 + m3
avg = total / 3

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

print(f"\nName: {name}")
print(f"Roll No: {roll}")
print(f"Total: {total:.2f}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")


name = input("Name: ")
roll = input("Roll No: ")

m1 = float(input("Marks subject 1: "))
m2 = float(input("Marks subject 2: "))
m3 = float(input("Marks subject 3: "))

total = m1 + m2 + m3
avg = total / 3

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

print(f"\nName: {name}")
print(f"Roll No: {roll}")
print(f"Total: {total:.2f}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
# ...existing code...