def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will throw an exception if the list is empty because it will try to divide by zero

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}")