import numpy as np
def calculate_total(data):
    subjects=["Python","SQL","Statistics"]
    data["Total"]=data[subjects].sum(axis=1)
    return data

def calculate_average(data):
    subjects=["Python","SQL","Statistics"]
    data["Average"]=np.round(data[subjects].mean(axis=1),2)
    return data

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >=50:
        return "D"
    else:
        return "F"

def assign_result(row):
    subjects=["Python","SQL","Statistics"]
    for s in subjects:
        if row[s]<35:
            return "Fail"
    return "Pass"

def calculate_statistics(data):
    subjects=["Python","SQL","Statistics"]
    overall_average=np.mean(data[subjects].to_numpy())
    highest_average=data["Average"].max()
    lowest_average=data["Average"].min()

    print("\n-------Class Statistics-------")
    print("Overall Class Average:",round(overall_average,2))
    print("Highest Student Average:",highest_average)
    print("Lowest Student Average:",lowest_average)

def subject_analysis(data):
    subjects=["Python","SQL","Statistics"]
    print("\n--------------Subject-wise Analysis------------")
    for s in subjects:
        average=np.mean(data[s])
        print(s,"Average:",round(average,2))

def display_top_students(data):
    print("\n-----------------Top 5 Students----------------")
    top_students=data.sort_values(by="Average",ascending=False).head(5)
    print(top_students[["Name","Total","Average","Grade"]]
          .to_string(index=False))
    