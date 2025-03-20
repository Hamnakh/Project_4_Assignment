def print_multiple(message: str, repeats: int):
    for i in range(repeats):  # repeats times loop chalega
        print(message)  # message print karega

# There is no need to edit code beyond this point
def main():
    message = input("Please type a message: ")  # User se message lena
    repeats = int(input("Enter a number of times to repeat your message: "))  # User se number lena
    print_multiple(message, repeats)  # Function call karna

if __name__ == "__main__":  # Yehi correct way hai
    main()
