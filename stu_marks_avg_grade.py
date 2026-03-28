
def get_marks():
    marks=[]
    for i in range(3):
        val=float(input(f"enter the marks of subject {i+1} out of 100: "))
        marks.append(val)
    return marks

def get_avg(marks):
    return round(sum(marks)/len(marks),2)


def get_grade(avg):
    if(avg>=85): return "A"
    elif(avg>=70): return "B"
    elif(avg>=50): return "C"
    else: return "D"






