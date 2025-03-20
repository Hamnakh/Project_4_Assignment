# User se ek number input lena
curr_value = int(input("Enter a number: "))

# Jab tak value 100 se chhoti hai, tab tak loop chalega
while curr_value < 100:
    curr_value = curr_value * 2  # Value ko double karna
    print(curr_value, end=" ")  # Ek hi line me output dena
