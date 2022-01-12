total_amount = float(input("Enter total amount: "))
number_of_people = int(input("Enter number of people: "))
print("Each person should pay: ", round(total_amount / number_of_people, 2))