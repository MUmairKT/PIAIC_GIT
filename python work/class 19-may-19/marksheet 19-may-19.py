# Marks sheet program using print input ifelse string 
strAry = []
print("Marks Calculation ")
stName=  input("Enter your name :")
english = int(input("Enter english Marks :"),10)
urdu = int(input("Enter english Marks :"),10)
maths = int(input("Enter english Marks :"),10)
science = int(input("Enter english Marks :"),10)
computer = int(input("Enter english Marks :"),10)
obtMarks = english+urdu+maths+science+computer
percentage = obtMarks/500*100
grade = ""
if percentage > 80:
    grade = "A"
elif percentage > 60:
    grade = "B"
elif percentage > 50:
    grade = "C"
elif percentage > 40:
    grade = "D"
elif percentage >= 35:
    grade = "E"
elif percentage < 35:
    grade = "F"
else :
    grade = "Null"

print((""" 
    ****************** Marks Sheet ***************
    Name : {}
    Marks Obtain  : {}  out of  {}
    Percentage : {}
    Grade : {}    
    
""").format(stName,obtMarks,"500",percentage,grade))

