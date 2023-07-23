def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers(start, end):
    primes = [num for num in range(start, end+1) if is_prime(num)]
    print("Prime numbers between", start, "and", end, "are:", primes)

if __name__ == "__main__":
    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        print_prime_numbers(start, end)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
