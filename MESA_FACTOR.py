def smallest_factor():
    while True:
        try:
            number = int(input("Enter an integer greater than or equal to 2: "))
            if number < 2:
                print("Invalid input. Please enter a number greater than or equal to 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    smallest_factor = None
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            smallest_factor = divisor
            break

    if smallest_factor is not None:
        return f"The smallest factor of {number} other than 1 is {smallest_factor}"
    else:
        return f"{number} is a prime number."
result = smallest_factor()
print(result)
