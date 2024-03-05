# Corrion 

 # Date

 # Assignment Name

 # A brief description of the project


my_list= []
x= float(input("Enter grade for Module 1:"))
print(my_list)
my_list.append(x)
x=float(input("Enter grade for module 2:"))
print(my_list)
my_list.append(x)
x=float(input("Enter grade for module 3:"))
print(my_list)
my_list.append(x)
x=float(input("Enter grade for mudle 4:"))
print(my_list)
my_list.append(x)
x=float(input("Enter grade for mudle 5:"))
print(my_list)
my_list.append(x)
x=float(input("Enter grade for mudle 6:"))
print(my_list)
my_list.append(x)
print('-'*12,"RESULTS",'-'*12)

lowest= min(my_list)
##lowest = format(lowest,',.2f')
print("Lowest Grade: " + str(format(lowest,',.2f')))

highest = max(my_list)
print("Highest Grade: ", highest)
length= len(my_list)
print(length)
sum1 = sum(my_list)
print("Sum of Grades: ",suml)
ave = sum1/length
print("Average: ", sum(my_list)/len(my_list))

