# # taking input 

import stu_marks_avg_grade as MAG
n=int(input("How many students: "))

students=[]

for i in range(n):
    print()
    name=input(f"Enter the name of the student {i+1}: ")
    marks=MAG.get_marks()
    avg=MAG.get_avg(marks)
    grade=MAG.get_grade(avg)

    students.append({
        "Name":name,
        "Marks":marks,
        "Average":avg,
        "Grade":grade
    })



print("\n----RESULT----")
for s in students:
    for key, value in s.items():
        print(key,"-->",value)
    print("--------")

