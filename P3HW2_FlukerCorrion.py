employee=input("Enter employee's name:")
hrs=float(input("Enter number of hours worked:"))
rate=float(input("Enter employee's pay rate:"))
print('_'*37)
print("Employee name:" + employee)
print("Headings")
print('-'*90)
print(hrs)
print(rate)



##ovt_hrs=0
##ovt_pay=0
if hrs>40:
    reg_pay=rate*40
    ovt_hrs=hrs-40
    ovt_rate=1.5*rate
    ovt_pay=ovt_hrs*ovt_rate
    gross_pay+reg_pay+ovt_pay
else:
    ovt_hrs=0
    ovt_pay=0
    reg_pay=rate*hrs
    gross_pay=reg_pay+ovt_pay

print("Hours worked   Pay Rate    Overtime    Overtime Pay        RegHour Pay         Gross Pay")


print(hrs)
print(rate)
print(ovt_hrs)
print(ovt_pay)
print(reg_pay)
print(gross_pay)
