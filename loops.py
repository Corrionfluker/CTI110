# for loops with validation and while loop to control iterations
choice='yes'
while choice.lower()=='yes':

    num= int(input("Enter the number of grades you would like to add up:"))
    total=0
    for i in range(1, num+1):
        grade= int(input("Enter grade#" + str(i)+","))
        while grade< 0 or grade>100:
         print("Grade must be between 1 and 100")
         print("Retry!")
         grade= int(input("Enter grade#" + str(i)+ "again"))
      total=total+grade
   ave=total/num
   print(ave)
   print(total)
     choice= input("Would you like to run the program again? Enter yes or no:")
    print("Program has excited!")          
