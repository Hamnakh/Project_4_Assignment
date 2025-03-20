def print_ones_digit(num):
    print("The ones digit is", num % 10)  # Num ka last digit print karega

def main():
    num = int(input("Enter a number: "))  # User se number lena
    print_ones_digit(num)  # Function call karna

if __name__ == "__main__":  # Correct syntax
    main()
