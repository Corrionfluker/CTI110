 # Corrion Fluker
 # 2/22/2024
 # P1HW2
 #This program calculates and displays travel expense



print("This program calculates and displays travel expenses")
print("")
budget=int(input("Enter Budget:"))
print("")
location=input("Enter your travel destination:")
print("")
gas=int(input("Hpw much do you think you will spend on gas?"))
print("")
hotel=int(input("Appprximatley, how much will you need for accomodations/hotel? "))
print("")
food=int(input("Last, how much do you ned for food? "))
print("")
print("------------Travel Expenses------------")
print("Location:" +str(location)+'.')
print("Initial Budget:" ,budget)
print("")
print("fuel:",gas)
print("Accomodation:" ,hotel)
print("Food;",food)
print("")
balance=budget-gas-hotel-food
print("Remaining balance:",balance)
print("Remaining Balance:", budget-gas-hotel-food)


##pseuedocode
##ger budget
##get location
##get food
