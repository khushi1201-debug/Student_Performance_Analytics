import pandas as pd
from functions import(calculate_total,calculate_average,assign_grade,assign_result,calculate_statistics,subject_analysis,display_top_students)

data=pd.read_csv("students.csv")

print("----------------------------------STUDENT PERFORMANCE ANALYTICS SYSTEM------------------------------------")

print("\n---------------------------Students Records--------------------------------")
print(data.to_string(index=False))

data=calculate_total(data)

data=calculate_average(data)

data["Grade"]=data["Average"].apply(assign_grade)

data["Result"]=data.apply(assign_result,axis=1)

print("\n-------------------Final Student Results-------------------------")

print(data[["Student_ID","Name","Total","Average","Grade","Result"]].to_string(index=False))

calculate_statistics(data)

subject_analysis(data)

print("\n----------PASS/FAIL Summary----------")

print("Students Passes:",(data["Result"]=="Pass").sum())
print("Students Fails:",(data["Result"]=="Fail").sum())

display_top_students(data)

data.to_csv("student_performance_results.csv",index=False)

print("\nFinal results saved successfully....")