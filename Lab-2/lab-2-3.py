name = input("Enter the name of the student : ")
roll_no = int(input("Enter the Roll No. of student : "))
marks = int(input("Enter the marks of student : "))
if(marks>=90):
    grade_point = 10
    grade_remark = "Outstanding"

elif(marks>=80 and marks<90):
    grade_point = 9
    grade_remark = "Very Good"

    
elif(marks>=80 and marks<90):
    grade_point = 9
    grade_remark = "Very Good"

elif(marks>=70 and marks<80):
    grade_point = 8
    grade_remark = "Good"

elif(marks>=60 and marks<70):
    grade_point = 7
    grade_remark = "Average"

elif(marks>=50 and marks<60):
    grade_point = 6
    grade_remark = "Pass"

elif( marks<50):
    grade_point = 0
    grade_remark = "Fail"



details = {
  "Name" : name,
   "Roll no" : roll_no,
   "Marks" : marks,
   "Grade Point" : grade_point,
   "Grade Remark" : grade_remark

}

for key, value in details.items():
    print(f"{key}: {value}")

