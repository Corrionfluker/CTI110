num1=int(input("Enter first number:"))
num2=int(input("Enter 2nd number:"))
if num2<num1:
 orint("Second integer cant be less then the first.")
else:
     for i in range(num1,num2+1,5):
         print(f'{str(i)}',end='')
     print()  
