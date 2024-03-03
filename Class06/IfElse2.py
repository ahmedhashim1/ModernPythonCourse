from typing import Union

PerType = Union[float, int]

percentages: list[PerType] = [88, 99.9, 50, 51.5, 65, 70]
grades: list[str] = []

for per in percentages:
    grade: str = ""
    if per >= 80:
        grade = "A+"
    elif per >= 70:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    elif per >= 40:
        grade = "D"
    elif per >= 33:
        grade = "E"
    else:
        grade = "Fail"

    grades.append(grade)

print(percentages)
print(grades)
