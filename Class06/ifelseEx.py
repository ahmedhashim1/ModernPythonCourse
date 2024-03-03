from typing import Union, Optional

# we can assign multiple types to Union
per: Union[int, float] = float(input("Enter your percentage: "))
# upper line can also re-written as
# per : int | float = 80 (with pipe character)
grade: Union[str, None] = None

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

print(f'Dear Student your percentage is {per}%, your grade is {grade}. ')
