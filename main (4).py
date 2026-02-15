from classes import PatientExam

#This gets the average bmi in the dataset
def avg_bmi(list_obj):
    bmi_total=0
    count=0
    for obj in list_obj:
        bmi_total+=obj.get_BMI()
        count+=1
    return bmi_total/count

#This gets the busiest month in the data set
def busy_month(list_obj):
    month_counts={}
    for exam in list_obj:
        month = exam.get_exam_month()   

        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1
    busiest= max(month_counts, key=month_counts.get)
    if busiest==1:
        return "January"
    elif busiest==2:
        return "February"
    elif busiest==3:
        return "March"
    elif busiest==4:
        return "April"
    elif busiest==5:
        return "May"
    elif busiest==6:
        return "June"
    elif busiest==7:
        return "July"
    elif busiest==8:
        return "August"
    elif busiest==9:
        return "September"
    elif busiest==10:
        return "October"
    elif busiest==11:
        return "November"
    elif busiest==12:
        return "December"


def main():
    exam=[]
    with open("patient_data.csv", mode='r', encoding= 'utf-8') as f:
        next(f)
        for line in f:
            exam.append(line.strip().split(","))
    patient_obj=[]
    for row in exam:
        obj = PatientExam(int(row[0]), row[1], row[2], int(row[3]), float(row[4]))
        patient_obj.append(obj)
    avg=avg_bmi(patient_obj)
    print(f"The average BMI is: {avg}")
    busy=busy_month(patient_obj)
    print(f"The busiest month is {busy}")
    


if __name__=="__main__":
    main()
